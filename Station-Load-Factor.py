"""
Problem: Station Load Factor
Difficulty: Hard

Description:
The input for this problem consists of n stations s1, ..., sn where 
station i (i = 1, 2, ..., n) is given by its integer coordinates 
xi and yi in the plane.

We say that station i can transmit to station j if station j is 
south-east of station i, i.e.,
xi < xj and yi > yj.

The load factor of station i is defined to be the number of stations 
it can transmit to.

The goal is to find a station with the largest load factor. If there
are several stations with the same largest load factor - return 
the list of those.

Task:
Give a divide and conquer algorithm for this problem. Your algorithm 
has to have worst case running time in o(n^2) (i.e. it must be 
asymptotically faster than quadratic time direct algorithm).

A brute-force solution that checks all n^2 pairs will have a
running time of Theta(n^2) and is not an acceptable solution.
"""

# --- YOUR o(n^2) SOLUTION GOES HERE ---

def find_max_load_stations(stations):
    """
    Finds the station(s) with the largest load factor using a
    divide-and-conquer algorithm.
    
    This algorithm must run in o(n^2) time (e.g., O(n log n)).
    
    Args:
        stations: A list of (x, y) tuples, where each tuple
                  represents the coordinates of a station.
                  
    Returns:
        A list of indices (from the original `stations` list)
        of the stations with the highest load factor. The order
        of indices in the returned list does not matter.
    """
    
    # Handle base cases
    if not stations:
        return []
    if len(stations) == 1:
        return stations # A single station has a load factor of 0
    stations = sorted(stations)
    stations_load = []
    for i in range(len(stations_load)):
        stations_load.append(0)
    stations, stations_loads = find_max_load_stations_aux(stations, stations_load)
    max_stations = []
    max_load = -1
    for i in range(len(stations_loads)):
        if stations_loads[i] > max_load:
            max_load = stations_loads[i]
            max_stations = [stations[i]]
        elif stations_loads[i] == max_load:
            max_stations.append(stations[i])
    return max_stations
def find_max_load_stations_aux(stations, stations_load):

    if len(stations) == 1:
        return stations, [0] # A single station has a load factor of 0
    mid = len(stations)//2
    left, leftLoads = find_max_load_stations_aux(stations[0:mid], stations_load[0: mid])
    right, rightLoads = find_max_load_stations_aux(stations[mid:len(stations)], stations_load[mid:len(stations_load)])

    mergeList = []
    i=0
    j=0
    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:
            mergeList.append(left[i])
            stations_load.append(leftLoads[i] + len(right)-j)
            i+=1
        else:
            mergeList.append(right[j])
            stations_load.append(0)
            j+=1

    while i < len(left):
        mergeList.append(left[i])
        stations_load.append(0)
        i+=1
    while j < len(right):
        mergeList.append(right[j])
        stations_load.append(0)
        j+=1
    return mergeList, stations_load
            
# --- Test Cases ---
# Format: (input_stations, expected_indices_with_max_load)
test_cases = [
    # Empty and Single Station
    ( [], [] ),
    ( [(1, 1)], [(1, 1)] ),

    # Simple Case - Clear Winner
    # s0(1,10) -> Load=2
    ( [(1, 10), (2, 5), (3, 1)], [(1, 10)] ),
    
    # No Transmissions (all have 0 load, so all are max)
    ( [(1, 1), (2, 2), (3, 3)], [(1, 1), (2, 2), (3, 3)] ),
    ( [(3, 1), (2, 2), (1, 3)], [(1, 3)] ),
    
    # Tie for Max Load
    # s0(1,10) -> Load=2
    # s2(0,8)  -> Load=2
    ( [(1, 10), (2, 5), (0, 8), (3, 1)], [(1, 10), (0, 8)] ),

    # Co-linear / Co-ordinate points (all 0)
    ( [(1, 5), (1, 2), (3, 5)], [(1, 5), (1, 2), (3, 5)] ),
    
    # More Complex Case
    # s2(1,8) -> Load=5
    ( [(3, 3), (5, 5), (1, 8), (8, 1), (6, 4), (4, 6)], [(1, 8)] ),
    
    # All same point (all 0)
    ( [(2, 2), (2, 2), (2, 2)], [(2, 2), (2, 2), (2, 2)] ),
    
    # Another simple tie
    # s0(1,5) -> Load=1
    # s1(0,7) -> Load=1
    ( [(1, 5), (0, 7), (2, 2)], [(0, 7)] ),
]

# --- Test Runner ---
def run_tests():
    print("Running tests...\n")
    passed_count = 0
    total_tests = len(test_cases)
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        try:
            actual_output = find_max_load_stations(test_input)
            
            # Sort for comparison, as order doesn't matter
            expected_set = set(expected_output)
            actual_set = set(actual_output)
            
            if actual_set == expected_set:
                print(f"[PASS] Test {i+1}")
                passed_count += 1
            else:
                print(f"[FAIL] Test {i+1}")
                print(f"       Input:    {test_input}")
                print(f"       Expected: {sorted(list(expected_set))}")
                print(f"       Got:      {sorted(list(actual_set))}")
                
        except Exception as e:
            print(f"[ERROR] Test {i+1}")
            print(f"        Input:    {test_input}")
            print(f"        Exception: {e}")
            
        print("-" * 20)

    print("\n--- Test Summary ---")
    print(f"{passed_count} / {total_tests} tests passed.")
    if passed_count == total_tests:
        print("All tests passed! 📡")
    else:
        print(f"{total_tests - passed_count} tests failed.")

# --- Execute the Tests ---
if __name__ == "__main__":
    run_tests()