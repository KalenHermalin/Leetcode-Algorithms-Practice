"""
Problem: Find Peak in a Bitonic Array
Difficulty: Medium

Description:
You are given an integer array `nums` that is guaranteed to be "bitonic".

A bitonic array is an array that first strictly increases and then, after 
reaching a single peak, may strictly decrease.

More formally, there exists some index `p` (where 0 <= p < len(nums)) such that:
- nums[0] < nums[1] < ... < nums[p]
- nums[p] > nums[p+1] > ... > nums[len(nums) - 1]

The array is guaranteed to have a single peak.

An array that is only strictly increasing (e.g., [1, 2, 3]) or only 
strictly decreasing (e.g., [3, 2, 1]) is also considered bitonic. 
In these cases, the peak is the maximum element.

Task:
Your task is to find and return the *value* of the peak element.

You must write an algorithm that runs in O(log n) time. A simple O(n) scan 
of the array is not an acceptable solution.

Examples:

Example 1:
Input: nums = [1, 4, 6, 9, 7, 3, 2]
Output: 9
Explanation: The array increases to 9 and then decreases. 9 is the peak.

Example 2:
Input: nums = [1, 2, 3, 4, 5]
Output: 5
Explanation: This is a strictly increasing array. The peak is the last element, 5.

Example 3:
Input: nums = [5, 4, 3, 2, 1]
Output: 5
Explanation: This is a strictly decreasing array. The peak is the first element, 5.

Example 4:
Input: nums = [1, 10, 3]
Output: 10

Constraints:

- 1 <= len(nums) <= 10**5
- -10**9 <= nums[i] <= 10**9
- It is guaranteed that `nums` is a bitonic array as defined above.
- For all valid `i`, nums[i] != nums[i+1] (i.e., adjacent elements are never equal).
"""

# Your O(log n) solution function goes here:
def find_peak_element(nums):
    # Find middle element
    if (len(nums) == 1): return nums[0];

    mid = (len(nums)-1)//2;

    if (nums[mid+1] > nums[mid]):
        return find_peak_element(nums[mid+1:len(nums)])
    if (nums[mid-1] > nums[mid]):
        return find_peak_element(nums[0:mid])
    else:
        return nums[mid]


# --- Test Cases ---
# Format: (input_array, expected_peak)
test_cases = [
    # General Bitonic Cases
    ([1, 4, 6, 9, 7, 3, 2], 9),
    ([1, 10, 3], 10),
    ([1, 2, 5, 6, 8, 12, 10, 9, 8, 4], 12),
    ([1, 3, 5, 7, 9, 11, 4, 2], 11),
    ([-10, -5, -1, 0, -2, -4, -8], 0),

    # Strictly Increasing / Decreasing Cases
    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 5),
    ([-5, -4, -3, -2, -1], -1),
    ([-1, -2, -3, -4, -5], -1),

    # Small Array / Boundary Cases
    ([100], 100),
    ([1, 10], 10),
    ([10, 1], 10),
    ([1, 10, 5], 10),
    ([1, 2, 3], 3),
    ([3, 2, 1], 3),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        try:
            actual_output = find_peak_element(test_input)
            
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
        print("All tests passed! 🎉")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    # If you haven't implemented the function yet, 
    # the tests will fail. That's expected!
    # Replace the placeholder function above with your logic.
    run_tests()