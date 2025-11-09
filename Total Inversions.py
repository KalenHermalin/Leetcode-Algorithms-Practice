"""
Problem: Count Inversions
Difficulty: Hard

Description:
An "inversion" in an array A is a pair of indices (i, j) such that
i < j but A[i] > A[j]. It's a pair of numbers that are "out of order."

Task:
Design a divide-and-conquer algorithm that counts the total number of 
inversions in an array. The brute-force method is Theta(n^2). 
Your algorithm must have a worst-case running time of o(n^2), 
which means O(n log n) is the target.

(Hint: This problem can be solved by modifying Mergesort. The "divide" 
and "conquer" parts are standard. The "combine" step is where you 
need to count the "split inversions" – inversions where one
element is in the left half and one is in the right half.)

Examples:

Example 1:
Input: A = [1, 5, 3, 2]
Output: 3
Explanation: The inversions are: (5, 3), (5, 2), and (3, 2).

Example 2:
Input: A = [1, 2, 3, 4]
Output: 0
Explanation: The array is already sorted, so there are no inversions.

Example 3:
Input: A = [4, 3, 2, 1]
Output: 6
Explanation: Every unique pair is an inversion:
(4, 3), (4, 2), (4, 1)
(3, 2), (3, 1)
(2, 1)
Total = 3 + 2 + 1 = 6.

Constraints:
- 1 <= A.length <= 10^5
- -10^9 <= A[i] <= 10^9
"""

# --- YOUR O(n log n) SOLUTION GOES HERE ---

def count_inversions(arr):
    """
    Public-facing function to start the inversion count.
    This function should implement (or call) a divide-and-conquer
    algorithm that runs in O(n log n) time.
    """
    if (len(arr) <= 1): return 0
    
    mid = len(arr)//2
    left, leftInv = countAndSortAux(arr[0:mid])
    right, rightInv = countAndSortAux(arr[mid:len(arr)])

    leftIndex=0
    rightIndex = 0
    crossInv = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if (left[leftIndex] < right[rightIndex]):
            leftIndex+=1;
        else:
            rightIndex+=1;
            crossInv+= len(left) - leftIndex;
    return crossInv + leftInv + rightInv

    
    

def countAndSortAux(arr):
    if (len(arr) == 1): return arr, 0

    mid = len(arr)//2
    left, leftInv = countAndSortAux(arr[0:mid])
    right, rightInv = countAndSortAux(arr[mid:len(arr)])

    leftIndex=0
    rightIndex = 0
    result = [];
    crossInv = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if (left[leftIndex] < right[rightIndex]):
            result.append(left[leftIndex])
            leftIndex+=1;
        else:
            result.append(right[rightIndex])
            rightIndex+=1;
            crossInv+= len(left) - leftIndex;
    
    while leftIndex < len(left):
        result.append(left[leftIndex])
        leftIndex+=1
    while rightIndex < len(right):
        result.append(right[rightIndex])
        rightIndex+=1;
        
    return result, crossInv + leftInv + rightInv


# --- Test Cases ---
# Format: (input_array, expected_inversions)
test_cases = [
    # User's Example
    ([1, 5, 3, 2], 3),

    # Empty and Single Element
    ([], 0),
    ([10], 0),

    # Sorted
    ([1, 2, 3, 4, 5], 0),
    ([-5, -1, 0, 10], 0),

    # Reverse Sorted
    ([2, 1], 1),
    ([3, 2, 1], 3),
    ([4, 3, 2, 1], 6),
    ([5, 4, 3, 2, 1], 10),

    # Mixed / General Cases
    ([2, 4, 1, 3, 5], 3), # (2,1), (4,1), (4,3)
    ([1, 20, 6, 4, 5], 5), # (20,6), (20,4), (20,5), (6,4), (6,5)
    ([8, 4, 2, 1], 6),
    ([3, 1, 2], 2),       # (3,1), (3,2)
    ([1, 3, 2, 4], 1),     # (3,2)
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        # Create a copy to avoid modifying the original test case
        arr_copy = list(test_input) 
        
        try:
            actual_output = count_inversions(arr_copy)
            
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
        print("All tests passed! 🚀")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()