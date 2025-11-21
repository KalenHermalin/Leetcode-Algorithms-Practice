"""
Problem: Search a 2D Sorted Matrix (n x n)
Difficulty: Medium

Description:
You are given an n x n matrix, `M`, where every row (left-to-right) 
and every column (top-to-bottom) is sorted in increasing order.

We need to find if a target value `X` is in the matrix.

Write an efficient algorithm that searches for this value. The
algorithm should be faster than O(n^2).

Example:
Given matrix =
[
  [ 1,  4,  7, 11],
  [ 2,  5,  8, 12],
  [ 3,  6,  9, 16],
  [10, 13, 14, 17]
]

If target = 9, return True.
If target = 20, return False.
"""

# --- YOUR EFFICIENT SOLUTION GOES HERE ---

def search_matrix(matrix, target):
    """
    Searches for a target value in an n x n matrix where rows
    and columns are sorted.
    
    This algorithm must run faster than O(n^2).
    The optimal solution is O(n).
    
    Args:
        matrix: A list of lists of integers, representing the n x n matrix.
        target: The integer to search for.
        
    Returns:
        True if the target is found, False otherwise.
    """
    
    # Handle edge cases
    if not matrix or not matrix[0]:
        return False
    n = len(matrix[0])
    row = 0
    column = n -1

    while row < n and column >= 0:
        currentValue = matrix[row][column]
        if currentValue == target: return True
        elif currentValue > target:
            column -= 1
        else:
            row+=1


    return False


# --- Test Cases ---
# Format: ((input_matrix, target), expected_output)
example_matrix_4x4 = [
  [ 1,  4,  7, 11],
  [ 2,  5,  8, 12],
  [ 3,  6,  9, 16],
  [10, 13, 14, 17]
]

matrix_3x3 = [
  [1, 5, 9],
  [3, 7, 10],
  [6, 8, 11]
]

test_cases = [
    # Problem Examples (4x4)
    ( (example_matrix_4x4, 9), True ),
    ( (example_matrix_4x4, 5), True ),
    ( (example_matrix_4x4, 20), False ),
    
    # Found at corners (4x4)
    ( (example_matrix_4x4, 1), True ),  # Top-left
    ( (example_matrix_4x4, 11), True ), # Top-right
    ( (example_matrix_4x4, 10), True ), # Bottom-left
    ( (example_matrix_4x4, 17), True ), # Bottom-right
    
    # Found in middle (4x4)
    ( (example_matrix_4x4, 8), True ),
    ( (example_matrix_4x4, 6), True ),

    # Not found (in range) (4x4)
    ( (example_matrix_4x4, 15), False ),
    ( (example_matrix_4x4, 0), False ),
    
    # 3x3 Matrix
    ( (matrix_3x3, 7), True ),
    ( (matrix_3x3, 11), True ),
    ( (matrix_3x3, 1), True ),
    ( (matrix_3x3, 6), True ),
    ( (matrix_3x3, 4), False ),
    ( (matrix_3x3, 12), False ),
    
    # Edge Case (1x1)
    ( ([[1]], 1), True ),
    ( ([[1]], 2), False ),
    
    # Edge Case (Empty list)
    ( ([], 1), False ),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        matrix, target = test_input  # Unpack the tuple
        
        try:
            actual_output = search_matrix(matrix, target)
            
            if actual_output == expected_output:
                print(f"[PASS] Test {i+1}")
                passed_count += 1
            else:
                print(f"[FAIL] Test {i+1}")
                print(f"       Input:    matrix={matrix}, target={target}")
                print(f"       Expected: {expected_output}")
                print(f"       Got:      {actual_output}")
                
        except Exception as e:
            print(f"[ERROR] Test {i+1}")
            print(f"        Input:    matrix={matrix}, target={target}")
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