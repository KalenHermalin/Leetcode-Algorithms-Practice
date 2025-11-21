"""
Problem: 3-SUM
Difficulty: Medium

Description:
You are given an array `A` of n integers and a single target integer `X`.
The problem is to determine if there exist three *different* indices 
i, j, and k such that A[i] + A[j] + A[k] = X.

The brute-force solution (checking every triplet) is Theta(n^3). 
Design an efficient algorithm that solves this problem with a time 
complexity of o(n^3) (e.g., O(n^2) or O(n^2 log n)).

(Hint: Think about how you could use your 2-SUM algorithm as a 
helper function.)

Examples:

Example 1:
Input: nums = [1, 2, 5, 10], target = 8
Output: true
Explanation: The triplet (1, 2, 5) from indices (0, 1, 2) sums to 8.

Example 2:
Input: nums = [-1, 0, 1, 2, -1, -4], target = 0
Output: true
Explanation: (-1, 0, 1) or (-1, 2, -1) sum to 0.

Example 3:
Input: nums = [1, 5, 10], target = 12
Output: false
Explanation: 1 + 1 + 10 = 12, but we cannot use the element at
index 0 twice. Indices must be different.
"""

# --- YOUR o(n^3) SOLUTION GOES HERE ---

def has_three_sum(nums, target):
    """
    Determines if three different elements in the list sum up to the target.
    This algorithm must run in o(n^3) time.
    
    Args:
        nums: A list of integers.
        target: The target sum.
        
    Returns:
        True if such a triplet exists, False otherwise.
    """
    if len(nums) < 3: return False
    nums = sorted(nums)
    for k in range(len(nums)):
        i = 0
        j = len(nums) - 1
        while i < j:
            if (i == k): i+=1
            if (j==k): j-=1
            if (i==j): continue
            if nums[i] + nums [j] < target - nums[k]:
                i+=1
            elif nums[i] + nums[j] > target - nums[k]:
                j-=1
            else:
                return True
    return False

# --- Test Cases ---
# Format: ((input_nums, target), expected_output)
test_cases = [
    # Problem Examples
    ( ([1, 2, 5, 10], 8), True ),
    ( ([-1, 0, 1, 2, -1, -4], 0), True ),
    ( ([1, 2, 3, 4], 11), False ),
    ( ([1, 5, 10], 12), False ), # Tests "different indices" rule

    # Basic Cases
    ( ([1, 2, 3], 6), True ),
    ( ([1, 2, 3], 7), False ),
    ( ([10, 1, 5, 2], 8), True ),  # 1 + 5 + 2
    ( ([12, 3, 4, 1, 6, 9], 24), True ), # 12 + 3 + 9
    
    # Edge Cases
    ( ([], 10), False ),           # Empty list
    ( ([1, 2], 10), False ),       # Fewer than 3 elements
    ( ([1, 2, 3], 5), False ),     # Exactly 3 elements, no match
    
    # Cases with Duplicates (testing "different indices")
    ( ([0, 0, 0], 0), True ),      # A[0]+A[1]+A[2]
    ( ([1, 1, 1], 3), True ),      # A[0]+A[1]+A[2]
    ( ([1, 1, 2], 4), True ),      # A[0]+A[1]+A[2]
    ( ([1, 1, 2], 5), False ),
    ( ([1, 5, 2, 1], 4), True ),   # 1 + 2 + 1 (indices 0, 2, 3)

    # Cases with Negatives
    ( ([-5, 1, 10, -2], 3), True ), # -5 + 1 + 10
    ( ([-1, -2, -3], -6), True ),
    ( ([-1, -2, -3], -5), False ),
    ( ([5, -2, 1, -10], 0), False ),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        nums, target = test_input  # Unpack the tuple
        
        try:
            actual_output = has_three_sum(nums, target)
            
            if actual_output == expected_output:
                print(f"[PASS] Test {i+1}")
                passed_count += 1
            else:
                print(f"[FAIL] Test {i+1}")
                print(f"       Input:    nums={nums}, target={target}")
                print(f"       Expected: {expected_output}")
                print(f"       Got:      {actual_output}")
                
        except Exception as e:
            print(f"[ERROR] Test {i+1}")
            print(f"        Input:    nums={nums}, target={target}")
            print(f"        Exception: {e}")
            
        print("-" * 20)

    print("\n--- Test Summary ---")
    print(f"{passed_count} / {total_tests} tests passed.")
    if passed_count == total_tests:
        print("All tests passed! 🚀")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()