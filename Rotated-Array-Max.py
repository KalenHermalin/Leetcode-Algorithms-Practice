"""
Problem: Find Max in a Circularly Shifted Array
Difficulty: Medium

Description:
Given a sorted in ascending order array `X[1..n]` of distinct integers,
the CRS (Circular Right Shift) operation was applied to it several times.

The CRS operation shifts all entries 1 position to the right, with the
last element moved to the first entry.

Example of CRS:
[1, 2, 3, 4, 5] --CRS--> [5, 1, 2, 3, 4] --CRS--> [4, 5, 1, 2, 3]

The number of times the CRS operation was applied is unknown.

Task:
Give an algorithm with complexity o(n) (strictly faster than n) to
find the largest value in this array.

NOTE: Your algorithm MUST have a running time of o(n). A simple
O(n) scan from left to right is not an acceptable solution.

Examples:

Input: X = [3, 4, 5, 1, 2]
Output: 5

Input: X = [5, 1, 2, 3, 4]
Output: 5

Input: X = [1, 2, 3, 4, 5]
Output: 5

Input: X = [2, 3, 4, 5, 1]
Output: 5

Constraints:
- 1 <= X.length <= 10^5
- All integers in X are distinct.
- The array was originally sorted in ascending order.
"""

# --- YOUR O(log n) SOLUTION GOES HERE ---

def find_max_in_rotated_array(nums):
    """
    Finds the largest value in a circularly shifted sorted array.
    This algorithm must run in O(log n) time.
    
    Args:
        nums: A list of distinct integers that was originally sorted
              and then circularly right-shifted.
        
    Returns:
        The largest integer in the list.
    """
    
    # Handle the edge case of an empty array, though constraints
    # say length >= 1.
    if not nums:
        return None
        
    if len(nums) == 1: return nums[0]
    mid = len(nums)//2
    if nums[mid] < nums[0]:
        return find_max_in_rotated_array(nums[0: mid])
    else:
        return find_max_in_rotated_array(nums[mid: len(nums)]) 



# --- Test Cases ---
# Format: (input_array, expected_max_value)
test_cases = [
    # General Cases
    ( ([3, 4, 5, 1, 2]), 5 ),
    ( ([4, 5, 1, 2, 3]), 5 ),
    
    # Peak at the beginning
    ( ([5, 1, 2, 3, 4]), 5 ),

    # Peak at the end (no rotation)
    ( ([1, 2, 3, 4, 5]), 5 ),
    
    # Peak just before the end
    ( ([2, 3, 4, 5, 1]), 5 ),
    
    # Larger arrays
    ( ([10, 12, 14, 20, 1, 3, 5, 8]), 20 ),
    ( ([5, 8, 10, 12, 14, 20, 1, 3]), 20 ),
    
    # Small Arrays
    ( ([1]), 1 ),
    ( ([1, 2]), 2 ),
    ( ([2, 1]), 2 ),
    
    # With negative numbers
    ( ([-1, -5, -4, -3, -2]), -1 ),
    ( ([-3, -2, -1, -5, -4]), -1 ),
    ( ([-5, -4, -3, -2, -1]), -1 ),
    ( ([10, 20, -5, 0, 5]), 20 ),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        try:
            actual_output = find_max_in_rotated_array(test_input)
            
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
    
        print("All tests passed! 🌀")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()