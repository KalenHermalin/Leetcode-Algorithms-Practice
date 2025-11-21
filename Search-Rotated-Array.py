"""
Problem: 33. Search in Rotated Sorted Array
Difficulty: Medium

Description:
You are given an array of n distinct integers that was *originally* sorted in ascending order. It was then **rotated** at some unknown 
pivot.

- Example: [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

You are also given a target value `X`. Your goal is to determine if 
`X` is in the array.

Task:
Write a function that searches for `X` in the array. If the target 
is found, return its index. Otherwise, return -1.

Your algorithm **must** have a running time of o(n), so a simple 
scan is not allowed. (This implies an O(log n) solution).

Examples:

Example 1:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Example 4:
Input: nums = [1, 2, 3, 4, 5], target = 2
Output: 1
(This is a sorted array with 0 rotations).

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of `nums` are unique.
- -10^4 <= target <= 10^4
"""

# --- YOUR O(log n) SOLUTION GOES HERE ---

def search_in_rotated_array(nums, target):
    """
    Searches for a target value in a rotated sorted array.
    This algorithm must run in O(log n) time.
    
    Args:
        nums: A list of distinct integers, originally sorted and
              then rotated at an unknown pivot.
        target: The integer to search for.
        
    Returns:
        True if target found, false otherwise
    """
    if len(nums) < 1: return False
    if len(nums) == 1: 
        if nums[0] == target:
            return True
        return False
    mid = len(nums)//2
    if nums[mid] == target: return True
    if nums[0] <= nums[mid]: # Left Side Sorted
        if nums[0] <= target <= nums[mid]:
            return search_in_rotated_array(nums[:mid], target)
        else:
            return search_in_rotated_array(nums[mid:], target)
    else:
        if nums[mid] <= target <= nums[len(nums)-1]:
            return search_in_rotated_array(nums[mid:], target)
        else:
            return search_in_rotated_array(nums[:mid], target)
        
    


    


# --- Test Cases ---
# Format: ((input_array, target), expected_index)
test_cases = [
    # Problem Examples
    ( ([4, 5, 6, 7, 0, 1, 2], 0), True ),
    ( ([4, 5, 6, 7, 0, 1, 2], 3), False ),
    ( ([1], 0), False ),

    # More targets in main example
    ( ([4, 5, 6, 7, 0, 1, 2], 4), True ),
    ( ([4, 5, 6, 7, 0, 1, 2], 2), True ),
    ( ([4, 5, 6, 7, 0, 1, 2], 5), True ),
    ( ([4, 5, 6, 7, 0, 1, 2], 1), True ),
    
    # Target not found (out of bounds)
    ( ([4, 5, 6, 7, 0, 1, 2], 8), False ),
    ( ([4, 5, 6, 7, 0, 1, 2], -1), False ),
    
    # No Rotation (standard binary search)
    ( ([1, 2, 3, 4, 5, 6], 4), True ),
    ( ([1, 2, 3, 4, 5, 6], 1), True ),
    ( ([1, 2, 3, 4, 5, 6], 6), True ),
    ( ([1, 2, 3, 4, 5, 6], 0), False ),
    
    # Different pivot
    ( ([7, 8, 1, 2, 3, 4, 5, 6], 8), True ),
    ( ([7, 8, 1, 2, 3, 4, 5, 6], 5), True ),
    ( ([7, 8, 1, 2, 3, 4, 5, 6], 0), False ),

    # Small Arrays (Edge Cases)
    ( ([1], 1), True ),
    ( ([1, 3], 1), True ),
    ( ([1, 3], 3), True ),
    ( ([1, 3], 2), False ),
    ( ([3, 1], 3), True ),
    ( ([3, 1], 1), True ),
    ( ([3, 1], 2), False ),
    
    # Empty Array
    ( ([], 5), False ),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        nums, target = test_input  # Unpack the tuple
        
        try:
            actual_output = search_in_rotated_array(nums, target)
            
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
        print("All tests passed! 🔍")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()