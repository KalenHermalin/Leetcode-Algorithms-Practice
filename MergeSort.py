"""
Problem: Implement Mergesort
Difficulty: Medium

Description:
Implement the Mergesort algorithm, a classic divide-and-conquer sorting
algorithm.

Task:
Write a function `mergesort(arr)` that takes a list of integers `arr`
and returns a *new* list containing the same elements, sorted in
non-decreasing (ascending) order.

Your algorithm must have a worst-case running time of O(n log n).
Your implementation should be "out-of-place" (it should not modify
the original input list).

The Algorithm (Divide and Conquer):
1.  **Divide:** Split the input list into two roughly equal halves.
2.  **Conquer:** Recursively sort the two halves by calling `mergesort`
    on them.
3.  **Combine:** Merge the two *sorted* halves back into a single,
    sorted list.

Example:
Input:  [8, 3, 1, 7, 0, 10, 2]
Output: [0, 1, 2, 3, 7, 8, 10]
"""

def mergeSort(arr):
    if (len(arr) <= 1): return arr

    mid = len(arr)//2
    left= mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:len(arr)])

    leftIndex=0
    rightIndex = 0
    result = [];
    while leftIndex < len(left) and rightIndex < len(right):
        if (left[leftIndex] < right[rightIndex]):
            result.append(left[leftIndex])
            leftIndex+=1
        else:
            result.append(right[rightIndex])
            rightIndex+=1
    while leftIndex < len(left):
        result.append(left[leftIndex])
        leftIndex+=1
    while rightIndex < len(right):
        result.append(right[rightIndex])
        rightIndex+=1;
        
    return result

# --- Test Cases ---
# Format: (input_array, expected_sorted_array)
test_cases = [
    # Empty Case
    ([], []),
    
    # Single Element
    ([5], [5]),
    
    # Already Sorted
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    
    # Reverse Sorted (Worst Case)
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([2, 1], [1, 2]),

    # With Duplicates
    ([5, 2, 5, 2, 5], [2, 2, 5, 5, 5]),
    ([4, 2, 3, 2, 4, 3, 3], [2, 2, 3, 3, 3, 4, 4]),
    
    # With Negative Numbers
    ([5, -2, 10, 0, -5], [-5, -2, 0, 5, 10]),
    ([-1, -5, -3], [-5, -3, -1]),
    
    # Odd Length Array
    ([8, 3, 1, 7, 0, 10, 2], [0, 1, 2, 3, 7, 8, 10]),
    
    # Even Length Array
    ([6, 5, 3, 1, 8, 7, 2, 4], [1, 2, 3, 4, 5, 6, 7, 8]),
    
    # All Same Elements
    ([4, 4, 4, 4], [4, 4, 4, 4]),
]

def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        # Create a copy to test that the original list is not modified
        arr_copy = list(test_input) 
        
        try:
            actual_output = mergeSort(arr_copy)
            
            # Check if the output is correct
            if actual_output == expected_output:
                # Check if the original list was modified
                if arr_copy != test_input:
                    print(f"[FAIL] Test {i+1} (Input list was modified)")
                    print(f"       Input:    {test_input}")
                    print(f"       Expected: {expected_output}")
                    print(f"       Got:      {actual_output}")
                    print(f"       Original list became: {arr_copy}")
                else:
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
        print("All tests passed!  sorting complete!  sorting complete! 🏆")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()