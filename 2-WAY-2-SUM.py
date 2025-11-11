"""
Problem: 2-WAY-2-SUM
Difficulty: Medium / Hard

Description:
In the 2-WAY-2-SUM decision problem, we are given two arrays, A and B, 
both of length n, containing (not necessarily distinct) integers.

We must determine whether there are two pairs of indices 
i1, i2, j1, j2 (all from {0, ..., n-1}) for which:

A[i1] + A[i2] = B[j1] + B[j2]

The indices are not necessarily distinct (e.g., i1 can equal i2).

Task:
Design an efficient algorithm that solves the 2-WAY-2-SUM problem and 
has a time complexity of o(n^3) (little-oh of n-cubed), which means
"strictly faster than n^3".

Note that the brute-force solution, which tries all possible quadruples
(i1, i2, j1, j2), has a running time of Theta(n^4). A less
straightforward solution that reduces the problem to 3-SUM might
run in Theta(n^3). Both of these solutions are too slow and would
be considered unacceptable.

(Hint: A successful algorithm will likely run in O(n^2 * log n) or O(n^2) time.
Think about the set of all possible sums from A, and the set of all
possible sums from B. How can you efficiently check if these two
sets have any values in common?)

Example:
A = [1, 5, 10]
B = [3, 3, 8]
Output: True
Explanation: A[0] + A[2] = 1 + 10 = 11. B[0] + B[2] = 3 + 8 = 11.

"""

# --- YOUR O(n^2 log n) or O(n^2) SOLUTION GOES HERE ---

def solve_2way_2sum(A, B):
    """
    Solves the 2-WAY-2-SUM problem in o(n^3) time.
    
    Args:
        A: A list of n integers.
        B: A list of n integers.
        
    Returns:
        True if indices (i1, i2, j1, j2) exist such that
        A[i1] + A[i2] = B[j1] + B[j2], False otherwise.
    """
    
    # Ensure arrays are of the same length
    if len(A) != len(B):
        # Or handle as an error, but for this problem, we assume n=len(A)=len(B)
        return False
        
    n = len(A)
    
    # Base case
    if n == 0:
        return False
    aSums = []
    bSums = []
    for i in range(n):
        for j in range(n):
            aSums.append(A[i] + A[j])            
            bSums.append(B[i] + B[j])            

    aSums = sorted(aSums)
    bSums = sorted(bSums)
    for i in range(n*n):
        if binary_search(bSums, aSums[i]) == True:
            return True;
    return False

def binary_search(arr, target): 
    n = len(arr)
    if n==1:
        if arr[0] == target: return True
        else: return False
    mid = n//2
    if arr[mid] < target:
        return binary_search(arr[mid:n], target)
    elif arr[mid] > target:
        return binary_search(arr[0:mid], target)
    else:
        return True
# --- Test Cases ---
# Format: ((Input_A, Input_B), Expected_Output)
test_cases = [
    # Basic True Cases
    ( ([1, 2], [1, 2]), True ),        # A[0]+A[1]=3, B[0]+B[1]=3
    ( ([1, 5], [2, 3]), True ),        # A[0]+A[1]=6, B[1]+B[1]=6
    ( ([8, 3], [5, 6]), True ),        # A[0]+A[1]=11, B[0]+B[1]=11
    ( ([1, 5, 10], [3, 3, 8]), True ), # A[0]+A[2]=11, B[0]+B[2]=11
    ( ([0, 5], [2, 3]), True ),        # A[1]+A[1]=10 (wrong) A[1]+A[0]=5, B[0]+B[1]=5

    # Basic False Cases
    ( ([1, 2], [3, 4]), False ),       # A sums: {2,3,4}, B sums: {6,7,8}
    ( ([10, 20], [1, 2]), False ),     # A sums: {20,30,40}, B sums: {2,3,4}
    ( ([8, 3], [5, 5]), False ),       # A sums: {6,11,16}, B sums: {10}
    
    # Edge Cases
    ( ([], []), False ),              # Empty arrays
    ( ([1], [1]), True ),             # Single element, 1+1 = 1+1
    ( ([1], [2]), False ),            # Single element, A sum=2, B sum=4

    # More Complex Cases
    ( ([1, 1, 1, 10], [2, 2, 2, 5]), False ), # A sums: {2, 11, 20}, B sums: {4, 7, 10}
    ( ([1, 1, 2, 10], [2, 2, 2, 5]), True ),  # A[0]+A[0]=2 (wrong) A[0]+A[1]=2, B[?]. A[2]+A[2]=4, B[0]+B[0]=4
    ( ([1, 10, 100, 1000], [0, 0, 0, 0]), False ), # A sums all > 0, B sums all = 0
    ( ([0, 0], [1, 1]), False ),       # A sum=0, B sums={2, 2}
    ( ([0, 1], [0, 0]), True ),        # A[0]+A[0]=0, B[0]+B[0]=0

    # Case with negative numbers
    ( ([-1, 5, 10], [3, -5, 8]), True ), # A[0]+A[2]=9, B[0]+B[2]=11. A[1]+A[1]=10, B[2]+B[2]=16. A[0]+A[1]=4, B[0]+B[1]=-2. A[1]+A[2]=15. B[0]+B[0]=6. B[1]+B[2]=3. Hmm. A[0]+A[2] = 9. B[0]+B[2] = 11. Let's find one.
                                          # A sums: {-2, 4, 9, 10, 15, 20}.
                                          # B sums: {-10, -2, 3, 6, 11, 16}.
                                          # Yes, -2 is common. A[0]+A[0] = -2. B[0]+B[1] = 3-5 = -2.
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        A, B = test_input  # Unpack the tuple
        
        try:
            actual_output = solve_2way_2sum(A, B)
            
            if actual_output == expected_output:
                print(f"[PASS] Test {i+1}")
                passed_count += 1
            else:
                print(f"[FAIL] Test {i+1}")
                print(f"       Input A:    {A}")
                print(f"       Input B:    {B}")
                print(f"       Expected: {expected_output}")
                print(f"       Got:      {actual_output}")
                
        except Exception as e:
            print(f"[ERROR] Test {i+1}")
            print(f"        Input A:    {A}")
            print(f"        Input B:    {B}")
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