"""
Problem: Significant Inversions
Difficulty: Hard

Description:
You are given an array A of n distinct integers.
We define a "Significant Inversion" as a pair of indices (i, j) such that:
    i < j  AND  A[i] > 3 * A[j]

Constraint:
Design a divide-and-conquer algorithm to count the number of significant
inversions in the array. Your algorithm must be asymptotically faster
than the quadratic brute force approach (i.e., o(n^2)).

(Hint: This is very similar to the standard "Count Inversions" problem.
You can modify Merge Sort. During the merge step, before merging the
two sorted subarrays, you can linearly scan to count how many elements
satisfy the condition A[i] > 3 * A[j].)

Examples:

Example 1:
Input: A = [10, 3, 1]
Output: 2
Explanation:
- (10, 3): 10 > 3*3 (10 > 9) -> True
- (10, 1): 10 > 3*1 (10 > 3) -> True
- (3, 1):   3 > 3*1 (3 > 3)  -> False

Example 2:
Input: A = [1, 2, 3]
Output: 0
Explanation: No pair satisfies the condition.

Example 3:
Input: A = [4, 1]
Output: 1
Explanation: 4 > 3*1 -> True.
"""

# --- YOUR o(n^2) SOLUTION GOES HERE ---

def count_significant_inversions(nums):
    """
    Counts the number of significant inversions in the array.
    Condition: i < j and nums[i] > 3 * nums[j].
    Must run in O(n log n) time.
    
    Args:
        nums: A list of distinct integers.
        
    Returns:
        The integer count of significant inversions.
    """
    
    # Handle base cases
    if len(nums) < 2:
        return 0
    result, sigInv = count_significant_inversions_aux(nums)
    return sigInv


def count_significant_inversions_aux(nums):
    n = len(nums)
    if (n <= 1): return nums, 0
    mid = n//2
    left, leftInv = count_significant_inversions_aux(nums[:mid])
    right, rightInv = count_significant_inversions_aux(nums[mid:])
    result = []
    sigInv = rightInv + leftInv
    r_index = 0
    for lVal in left: # Loops through n/2 items
        while r_index < len(right) and lVal > 3 * right[r_index]: # Loops a max of n/2 items
            r_index+=1
        sigInv += r_index
    # ^^Above is O(n), it loops thorugh each value in left (n/2 items) and checks if that value is greater than 3 * rights value
    #  if it is it increases the right index and checks the next, and so on until it isnt bigger. Not the right index tracked the amount of significant inversions for that element
    i=0 
    j=0

    # Classic Merge Sort (listed need to be sorted to count cross inversions on next layer)
    while i < len(left) and j < len(right):
        if (left[i] >  right[j]): #Inversion
            result.append(right[j])
            j+=1
        
        else:
            result.append(left[i])
            i+=1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1  
    return result, sigInv
            
            
# --- Test Cases ---
# Format: (input_array, expected_count)
test_cases = [
    # Basic Cases
    ( ([10, 3, 1]), 2 ),
    ( ([1, 2, 3]), 0 ),
    ( ([3, 2, 1]), 0 ), # Standard inversions exist, but no significant ones (3 !> 6, 3 !> 3, 2 !> 3)

    # Edge Cases
    ( ([4, 1]), 1 ),     # 4 > 3
    ( ([3, 1]), 0 ),     # 3 is not > 3
    ( ([30, 10]), 0 ),   # 30 is not > 30
    ( ([31, 10]), 1 ),   # 31 > 30

    # Larger Mix
    # (10, 5) -> 10 > 15 (No)
    # (10, 1) -> 10 > 3  (Yes)
    # (5, 1)  -> 5 > 3   (Yes)
    ( ([10, 5, 1]), 2 ),

    # Ascending Order (Impossible to have i < j AND A[i] > A[j]*3 if all pos)
    ( ([1, 5, 10, 20]), 0 ),
    
    # Negative Numbers (Careful with multiplication!)
    # i=0, j=1. A[i]=-5, A[j]=-10. 
    # Condition: -5 > 3*(-10) => -5 > -30. True.
    ( ([-5, -10]), 1 ),
    
    # i=0, j=1. A[i]=-10, A[j]=-5.
    # Condition: -10 > 3*(-5) => -10 > -15. True.
    ( ([-10, -5]), 1 ),
    
    # Empty / Single
    ( ([]), 0 ),
    ( ([5]), 0 ),
    
    # Complex Case
    # [50, 20, 10, 3, 1]
    # 50 vs 20 (No: 50 !> 60)
    # 50 vs 10 (Yes: 50 > 30)
    # 50 vs 3  (Yes: 50 > 9)
    # 50 vs 1  (Yes: 50 > 3)
    # 20 vs 10 (No: 20 !> 30)
    # 20 vs 3  (Yes: 20 > 9)
    # 20 vs 1  (Yes: 20 > 3)
    # 10 vs 3  (Yes: 10 > 9)
    # 10 vs 1  (Yes: 10 > 3)
    # 3 vs 1   (No: 3 !> 3)
    # Total: 3 + 2 + 2 = 7
    ( ([50, 20, 10, 3, 1]), 7 ),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        # Create a copy to protect against in-place modification
        nums_copy = list(test_input)
        
        try:
            actual_output = count_significant_inversions(nums_copy)
            
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
        print("All tests passed! 📉")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()