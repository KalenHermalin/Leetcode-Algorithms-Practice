"""
Problem: 53. Maximum Subarray
Difficulty: Medium

Description:
Given an integer array `nums`, find the contiguous subarray
(containing at least one number) which has the largest sum 
and return its sum.

A subarray is a contiguous part of an array.

The brute-force solution (checking the sum of all possible
subarrays) is Theta(n^2).

Task:
Design an efficient algorithm that solves this problem with a 
running time of o(n^2). Both the O(n log n) divide-and-conquer 
approach and the O(n) linear scan (Kadane's algorithm) 
are acceptable.

Examples:

Example 1:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum = 1.

Example 3:
Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The subarray [5, 4, -1, 7, 8] (the entire array)
has the largest sum = 23.

Example 4:
Input: nums = [-2, -1, -3, -5]
Output: -1
Explanation: The subarray [-1] has the largest sum = -1.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# --- YOUR o(n^2) SOLUTION GOES HERE ---
def find_max_subarray(A):
    if len(A) == 1:
        return A[0]
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]

    leftMax = find_max_subarray(left)
    rightMax = find_max_subarray(right)

    maxLeftCrossing = -float("inf")
    currentSum = 0
    for i in range(mid-1, -1,-1):
        currentSum += A[i]
        if currentSum > maxLeftCrossing:
            maxLeftCrossing = currentSum
    maxRightCrossing = -float("inf")
    currentSum = 0
    for i in range(mid, len(A)):
        currentSum += A[i]
        if currentSum > maxRightCrossing:
            maxRightCrossing = currentSum
    maxCrossing = maxLeftCrossing + maxRightCrossing
    return max(maxCrossing, leftMax, rightMax)

# --- Test Cases ---
# Format: (input_array, expected_max_sum)
test_cases = [
    # Problem Examples
    ( ([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6 ),
    ( ([1]), 1 ),
    ( ([5, 4, -1, 7, 8]), 23 ),
    
    # All Negative Numbers
    ( ([-2, -1, -3, -5]), -1 ),
    ( ([-1, -2, -3]), -1 ),
    ( ([-10]), -10 ),

    # All Positive Numbers
    ( ([1, 2, 3, 4, 5]), 15 ),
    
    # Mixed cases
    ( ([1, 2, -1, -2, 2, 1, -2, 1]), 3 ), # 2, 1
    ( ([5, -3, 5]), 7 ), # 5, -3, 5
    ( ([1, -1, 1]), 1 ),
    ( ([-1, 1, 0, 1, -1]), 2 ), # 1, 0, 1
    ( ([8, -19, 5, -4, 20]), 21 ), # 5, -4, 20
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        try:
            actual_output = find_max_subarray(test_input)
            
            if actual_output == expected_output:
                print(f"[PASS] Test {i+1}")
                passed_count += 1
            else:
                print(f"[FAIL] Test {i+1}")
                print(f"       Input:    {test_input}")
                print(f"       Expected: {expected_output}")
                print(f"       Got:      {actual_output}")
                
        except Exception as e:
            print(f"[ERROR] Test {i+1}")
            print(f"        Input:    {test_input}")
            print(f"        Exception: {e}")
            
        print("-" * 20)

    print("\n--- Test Summary ---")
    print(f"{passed_count} / {total_tests} tests passed.")
    if passed_count == total_tests:
        print("All tests passed! 📈")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()