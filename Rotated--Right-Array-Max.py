def find_max_in_rotated_array(A):
    left = 0
    right = len(A) -1 
    while left <= right:
        mid = (left+right)//2
        if (A[mid] < A[left]):
            right = mid
        else:
            left = mid -1

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