def count_inversions(A):
    if len(A) <1:
        return 0, A
    if len(A) == 1:
        return 0, A
    
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]
    leftInversions, leftSorted = count_inversions(left)
    rightinversions, rightSorted = count_inversions(right)
    i = 0
    j=0
    crossInversions = 0
    res = []
    while i < len(leftSorted) and j < len(rightSorted):
        if leftSorted[i] < rightSorted[j]:
            res.append(leftSorted[i])
            i+=1
        else:
            res.append(rightSorted[j])
            crossInversions += len(leftSorted) - i
            j+=1
    while i < len(leftSorted):
        res.append(leftSorted[i])
        i+=1
    while j < len(rightSorted):
        res.append(rightSorted[j])
        j+=1
    return crossInversions + leftInversions + rightinversions, res


test_cases = [
    # User's Example
    ([1, 5, 3, 2], (3, [1, 2,3 ,5])),

    # Empty and Single Element
    ([], (0, [])),
    ([10], (0, [10])),

    # Sorted
    ([1, 2, 3, 4, 5], (0, [1,2,3,4,5])),
    ([-5, -1, 0, 10], (0, [-5, -1, 0, 10])),

    # Reverse Sorted
    ([2, 1], (1, [1,2])),
    ([3, 2, 1], (3, [1,2,3])),
    ([4, 3, 2, 1], (6,[1,2,3,4])),
    ([5, 4, 3, 2, 1], (10, [1,2,3,4,5])),

    # Mixed / General Cases
    ([2, 4, 1, 3, 5], (3, [1,2,3,4,5])), # (2,1), (4,1), (4,3)
    ([1, 20, 6, 4, 5], (5, [1,4,5,6,20])), # (20,6), (20,4), (20,5), (6,4), (6,5)
    ([8, 4, 2, 1], (6, [1,2,4,8])),
    ([3, 1, 2], (2, [1,2,3])),       # (3,1), (3,2)
    ([1, 3, 2, 4], (1, [1,2,3,4])),     # (3,2)
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