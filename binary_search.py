"""
Problem: Binary Search
Difficulty: Easy

Description:
Given a sorted array of integers `nums` (in ascending order) and an
integer `target`, write a function to search for `target` in `nums`.

Task:
If the `target` exists, return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Examples:

Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in `nums` are unique. (We will add non-unique
  test cases, but you can assume uniqueness for the basic problem)
- `nums` is sorted in ascending order.
"""

# --- YOUR O(log n) SOLUTION GOES HERE ---

def binary_search_recrusive(nums, target):
    """
    Searches for a target value in a sorted list of integers
    using the Binary Search algorithm.
    
    Args:
        nums: A list of integers sorted in ascending order.
        target: The integer to search for.
        
    Returns:
        The index of the target if found, otherwise -1.
    """
    
    # TODO: Implement your O(log n) binary search logic.
    n = len(nums)
    if n == 0: return -1
    if n==1:
        if nums[0] == target: return 0
        else: return -1
    mid = n//2
    if nums[mid] < target:
        index = binary_search_recrusive(nums[mid:n], target)
        if index > -1:
            return mid + index
        return index
    elif nums[mid] > target:
        index =  binary_search_recrusive(nums[0:mid], target)
        return index
    else:
        return mid

def binary_search_iterative(nums, target):
    n = len(nums)
    if (n < 1): return -1
    if (n==1):
        if nums[0] == target: return 0
        return -1
   # DO IT WITOUT RECURSION MIGHT BE EASIER
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target: 
            return mid
        elif nums[mid] < target: 
                left = mid + 1
        else:
                right = mid - 1
    return -1

# --- Test Cases ---
# Format: ((input_array, target), expected_index)
test_cases = [
    # Basic Cases
    ( ([-1, 0, 3, 5, 9, 12], 9), 4 ),
    ( ([-1, 0, 3, 5, 9, 12], 2), -1 ),

    # Empty Array
    ( ([], 5), -1 ),

    # Single Element
    ( ([5], 5), 0 ),
    ( ([5], 3), -1 ),

    # Target at Boundaries
    ( ([1, 2, 3, 4, 5], 1), 0 ),   # Target at the beginning
    ( ([1, 2, 3, 4, 5], 5), 4 ),   # Target at the end
    
    # Even and Odd Length Arrays
    ( ([1, 2, 3, 4, 5, 6], 4), 3 ), # Even length, target in right half
    ( ([1, 2, 3, 4, 5, 6], 2), 1 ), # Even length, target in left half
    ( ([1, 2, 3, 4, 5], 4), 3 ),   # Odd length, target in right half
    ( ([1, 2, 3, 4, 5], 2), 1 ),   # Odd length, target in left half
    ( ([1, 2, 3, 4, 5], 3), 2 ),   # Odd length, target at middle
    
    # Target Not Found (in gaps or out of bounds)
    ( ([2, 5, 7, 8, 11, 12], 1), -1 ), # Target smaller than all elements
    ( ([2, 5, 7, 8, 11, 12], 13), -1 ),# Target larger than all elements
    ( ([2, 5, 7, 8, 11, 12], 6), -1 ), # Target in a "gap"
    ( ([2, 5, 7, 8, 11, 12], 0), -1 ), # Target is 0, not present

    # With Duplicates (standard binary search will find *an* index)
    # Note: The problem description says unique, but we test this anyway.
    # The exact index found (e.g., 2, 3, or 4) can vary by implementation.
    # We will test against one valid possibility.
    ( ([1, 2, 5, 5, 5, 8], 5), 3 ), # A valid index for 5 is 2, 3, or 4.
                                   # The typical (left+right)//2 finds index 3.
    ( ([5, 5, 5, 5, 5], 5), 2 ),   # A valid index is 0-4. Middle is 2.
    ( ([1, 2, 2, 2, 3], 4), -1 ),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        nums, target = test_input  # Unpack the tuple
        
        try:
            actual_output = binary_search_recrusive(nums, target) # binary_search_iterative
            
            # Special check for duplicate case
            is_pass = False
            if nums == [1, 2, 5, 5, 5, 8] and target == 5:
                if actual_output in [2, 3, 4]:
                    is_pass = True
            elif nums == [5, 5, 5, 5, 5] and target == 5:
                 if actual_output in [0, 1, 2, 3, 4]:
                    is_pass = True
            else:
                if actual_output == expected_output:
                    is_pass = True

            if is_pass:
                print(f"[PASS] Test {i+1}")
                passed_count += 1
            else:
                print(f"[FAIL] Test {i+1}")
                print(f"       Input:    nums={nums}, target={target}")
                print(f"       Expected: {expected_output}")
                print(f"       Got:      {actual_output}")
                if nums == [1, 2, 5, 5, 5, 8] and target == 5:
                    print("       (Note: Any index from {2, 3, 4} is acceptable)")
                
        except Exception as e:
            print(f"[ERROR] Test {i+1}")
            print(f"        Input:    nums={nums}, target={target}")
            print(f"        Exception: {e}")
            
        print("-" * 20)

    print("\n--- Test Summary ---")
    print(f"{passed_count} / {total_tests} tests passed.")
    if passed_count == total_tests:
        print("All tests passed! 🎯")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()