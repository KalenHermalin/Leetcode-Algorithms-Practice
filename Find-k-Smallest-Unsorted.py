"""
Problem: 215. Kth Largest Element in an Array (Modified)
Difficulty: Medium

Description:
The problem is to find the k-th smallest element in an unsorted array.
You are given an array of n integers, `nums`, and an integer `k`.
Your goal is to find the k-th smallest element.

Note that `k` is 1-indexed, so:
- If k = 1, we want the 1st smallest element (the minimum).
- If k = n, we want the n-th smallest element (the maximum).

Task:
Design an algorithm with a worst-case running time of o(n log n)
(strictly faster than n log n). The "obvious" way is to sort the
array, which is O(n log n), so we need to do better.

A successful algorithm will have an average-case running time of O(n).

Examples:

Example 1:
Input: A = [8, 1, 9, 4, 3, 6], k = 1
Output: 1
Explanation: The 1st smallest element (the min) is 1.

Example 2:
Input: A = [8, 1, 9, 4, 3, 6], k = 3
Output: 4
Explanation: The 3rd smallest element is 4.
(Sorted: [1, 3, 4, 6, 8, 9])

Example 3:
Input: A = [8, 1, 9, 4, 3, 6], k = 6
Output: 9
Explanation: The 6th smallest element (the max) is 9.

Example 4:
Input: A = [3, 2, 1, 5, 6, 4], k = 2
Output: 2

Constraints:
- 1 <= k <= nums.length
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

# --- YOUR O(n) AVERAGE-CASE SOLUTION GOES HERE ---

def find_kth_smallest(A, k):
    """
    Finds the k-th smallest element in an unsorted array.
    'k' is 1-indexed (k=1 is the minimum).
    Must run in O(n) average time (o(n log n)).
    
    Args:
        nums: A list of integers.
        k: The 1-indexed rank of the element to find.
        
    Returns:
        The k-th smallest element.
    """
    if len(A) == 1:
        return A[0]
    pivot_index = partition(A)
    rank = pivot_index + 1
    if k == rank:
        return A[pivot_index]
    if rank > k:
        return find_kth_smallest(A[:pivot_index], k)
    else:
        return find_kth_smallest(A[pivot_index+1: ], k-rank)

def partition(A):
    # Chooses a pivot value (the last element for simplicity)
    pivotValu = A[len(A)-1]
    boundry = 0 # index to the left smaller than pivot, to the right is bigger
    for i in range(len(A)-1):
        if A[i] < pivotValu: # Else do nothing, value is big -> leave in big section
            #Swap A[i] with the value at the boundry, because the value belongs in small side
            A[i], A[boundry] = A[boundry], A[i] 
            # Icrease boundry to protect the element we just put to the small side
            boundry+=1
    # boundry now points to the start of the "bigger than" section
    # The pivot is still at the end of the array. Since this is out pivot
    # Its correct posisiton should be inbetween the small and the big sections
    # Boundry already points there so we swap
    A[len(A)-1], A[boundry] = A[boundry], A[len(A)-1]
    return boundry
# --- Test Cases ---
# Format: ((input_array, k), expected_output)
test_cases = [
    # Problem Examples from screenshot
    ( ( [8, 1, 9, 4, 3, 6], 1 ), 1 ),
    ( ( [8, 1, 9, 4, 3, 6], 3 ), 4 ),
    ( ( [8, 1, 9, 4, 3, 6], 6 ), 9 ),

    # Standard LeetCode example
    ( ( [3, 2, 1, 5, 6, 4], 2 ), 2 ),
    
    # k=min and k=max
    ( ( [3, 2, 1, 5, 6, 4], 1 ), 1 ),
    ( ( [3, 2, 1, 5, 6, 4], 6 ), 6 ),
    
    # With Duplicates
    ( ( [3, 2, 3, 1, 2, 4, 5, 5, 6], 1 ), 1 ), # k=min
    ( ( [3, 2, 3, 1, 2, 4, 5, 5, 6], 9 ), 6 ), # k=max
    ( ( [3, 2, 3, 1, 2, 4, 5, 5, 6], 5 ), 3 ), # Sorted: [1,2,2,3,3,4,5,5,6], 5th is 3
    ( ( [3, 2, 3, 1, 2, 4, 5, 5, 6], 2 ), 2 ), # 2nd is 2
    
    # Small Arrays
    ( ( [1], 1 ), 1 ),
    ( ( [2, 1], 1 ), 1 ),
    ( ( [2, 1], 2 ), 2 ),
    
    # Pre-sorted and reverse-sorted
    ( ( [1, 2, 3, 4, 5, 6, 7], 4 ), 4 ),
    ( ( [7, 6, 5, 4, 3, 2, 1], 3 ), 3 ),
    ( ( [7, 6, 5, 4, 3, 2, 1], 1 ), 1 ),
    ( ( [7, 6, 5, 4, 3, 2, 1], 7 ), 7 ),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        nums, k = test_input
        # Create a copy so the original test case is not modified
        # by an in-place algorithm (which Quickselect often is)
        nums_copy = list(nums) 
        
        try:
            actual_output = find_kth_smallest(nums_copy, k)
            
            if actual_output == expected_output:
                print(f"[PASS] Test {i+1}")
                passed_count += 1
            else:
                print(f"[FAIL] Test {i+1}")
                print(f"       Input:    nums={nums}, k={k}")
                print(f"       Expected: {expected_output}")
                print(f"       Got:      {actual_output}")
                
        except Exception as e:
            print(f"[ERROR] Test {i+1}")
            print(f"        Input:    nums={nums}, k={k}")
            print(f"        Exception: {e}")
            
        print("-" * 20)

    print("\n--- Test Summary ---")
    print(f"{passed_count} / {total_tests} tests passed.")
    if passed_count == total_tests:
        print("All tests passed! ⚡")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()