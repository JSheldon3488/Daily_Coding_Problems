"""
Date: 8/27/20
14.3: Count Android Unlock Combinations
"""

'''
Problem Statement: One way to unlock an Android phone is by swiping in a specific pattern across a 1-9 keypad.
For a pattern to be valid it must satisfy the following criteria:
    1. All of its keys must be distinct
    2. It must not connect two keys by jumping over a third key, unless that key has already been used.
    
Example:
    [1,2,3
     4,5,6          4->2->1->7 Valid
     7,8,9]         2->1->7 Invalid (because it would have to skip over 4

Find the total number of valid unlock patters of length n, where 1 <= n = 9
'''

'''                             My Solution                              '''
""" First off I want to represent the keypad as a dictionary of (row,col) -> value. Example d[(0,0)]  = 1

I think the algorithm is going to be start with all valid numebrs for this level and recursively call on an updated valid list
and used list until you get to n=1 level and at that level you know there are len(valid) combos to get there. This feels kind of brute
force search but I think it prunes a little by only pursuing forward valid cases. The hard part is going to be writing the
get_valid function that follows the two rules above. First we know that we need the keys to be distinct which is easy if we just
pass forward a list of the ones we already used. The second one is much trickier, the valid options will be one row to the left or right
and one column up or down UNLESS that value for the cell next you are looking at is in used then we can go two away.

Honestly this get_valid function feels really bad. I think the rest of my algorithm is fine, but this get_valid just feels
really expensive. Also the back tracking is on the used variable.         
"""
from typing import List
BOARD = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9}

def count_android_combos(n: int, used=[], valid=[1,2,3,4,5,6,7,8,9]):
    if n == 1:
        return len(valid)

    total = 0
    for row in range(3):
        for col in range(3):
            if BOARD[(row, col)] in valid:
                used.append(BOARD[(row, col)])
                next_valid = get_valid(row, col, used)
                total += count_android_combos(n-1, used, next_valid)
                used = used[:-1]
    return total

def get_valid(row: int, col: int, used: List[int]) -> List[int]:
    valid = []
    # Get valid from row
    #Left Check
    if (row-1, col) in BOARD:
        if BOARD[(row-1,col)] not in used:
            valid.append(BOARD[(row-1,col)])
        elif (row-2, col) in BOARD and BOARD[(row-2,col)] not in used:
            valid.append(BOARD[(row-2,col)])
    #Right Check
    if (row+1, col) in BOARD:
        if BOARD[(row+1, col)] not in used:
            valid.append(BOARD[(row+1, col)])
        elif (row+2, col) in BOARD and BOARD[(row+2, col)] not in used:
            valid.append(BOARD[(row+2,col)])

    # Get valid from col
    #UP Check
    if (row, col-1) in BOARD:
        if BOARD[(row,col-1)] not in used:
            valid.append(BOARD[(row,col-1)])
        elif (row, col-2) in BOARD and BOARD[(row,col-2)] not in used:
            valid.append(BOARD[(row,col-2)])
    #Down Check
    if (row, col+1) in BOARD:
        if BOARD[(row, col+1)] not in used:
            valid.append(BOARD[(row, col+1)])
        elif (row, col+2) in BOARD and BOARD[(row, col+2)] not in used:
            valid.append(BOARD[(row,col+2)])

    # Get valid diagonal
    # Up Left Check
    if (row-1, col-1) in BOARD:
        if BOARD[(row-1,col-1)] not in used:
            valid.append(BOARD[(row-1,col-1)])
        elif (row-2, col-2) in BOARD and BOARD[(row-2,col-2)] not in used:
            valid.append(BOARD[(row-2, col-2)])
    # Up Right Check
    if (row+1, col-1) in BOARD:
        if BOARD[(row+1, col-1)] not in used:
            valid.append(BOARD[(row+1, col-1)])
        elif (row+2, col-2) in BOARD and BOARD[(row+2, col-2)] not in used:
            valid.append(BOARD[(row+2,col-2)])
    # Down Left Check
    if (row-1, col+1) in BOARD:
        if BOARD[(row-1, col+1)] not in used:
            valid.append(BOARD[(row-1, col+1)])
        elif (row-2, col+2) in BOARD and BOARD[(row-2, col+2)] not in used:
            valid.append(BOARD[(row-2, col+2)])
    # Down Right Check
    if (row+1, col+1) in BOARD:
        if BOARD[(row+1, col+1)] not in used:
            valid.append(BOARD[(row+1, col+1)])
        elif (row+2, col+2) in BOARD and BOARD[(row+2, col+2)] not in used:
            valid.append(BOARD[(row+2, col+2)])

    return valid


'''                             Book Solution                            '''
""" There is a symmetry improvement because 1,3,7,9 are all the same as is 2,4,6,8."""
def num_paths(current, jumps, visited, n):
    if n == 1:
        return 1

    paths = 0
    for number in range(1,10):
        if number not in visited:
            if (current, number) not in jumps or jumps[(current, number)] in visited:
                visited.add(number)
                paths += num_paths(number, jumps, visited, n-1)
                visited.remove(number)
    return paths

def unlock_combinations(n):
    jumps = {
        (1,3): 2, (1,7): 4, (1,9): 5,
        (2,8): 5,
        (3,1): 2, (3,7): 5, (3,9): 6,
        (4,6): 5, (6,4): 5,
        (7,1): 4, (7,3): 5, (7,9): 8,
        (8,2): 5,
        (9,1): 5, (9,3): 6, (9,7): 8 }
    return 4 * num_paths(1, jumps, {1}, n) + \
           4 * num_paths(2, jumps, {2}, n) + \
           1 * num_paths(5, jumps, {5}, n)

'''                             Test Cases                               '''



def main():
    print(count_android_combos(1))
    print(count_android_combos(2))
    print(count_android_combos(3))

    # Their answer is actually incorrect.
    print(unlock_combinations(1))
    print(unlock_combinations(2))
    print(unlock_combinations(3))

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * In problems like this always look for symmetry so that you can do less work.
    * 
'''

