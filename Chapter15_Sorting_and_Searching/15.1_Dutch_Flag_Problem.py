"""
Date: 9/7/20
15.1 Dutch Flag Problem
"""

'''
Problem Statement: Given an array of strictly the characteres 'R', 'G', 'B', segregate the values of the array so that
all the Rs come first, the G's come second, and the B's come last. You can only swap elements of the array. Do this
in linear time and in-place.

Example: ['G', 'B', 'R', 'R', 'B', 'R', 'G'] returns ['R', 'R', 'R', 'G', 'G', 'B', 'B']
'''

'''                             My Solution                              '''
''' I think this is a good place to use the two pointer slow fast concept. Start with both pointing at the 0 index. If
this index value is the first char you are looking for R in this case, then you can move on to the next index otherwise you leave
the slow index here and move the fast index forward looking for an R to swap the slow index with. When you perform the swap
you move both index's forward. Once you get to the end of the array with the fast pointer you know all the Rs are in place and
you reset the fast pointer to the slow pointer and start the process over for G. Once you finish this process for G you are done and
do not even need to do it for B because they will be in the right place by default.'''
from typing import List

def dutch_flag(flags: List[str]):
    slow, fast = 0, 0
    goal = 'R'

    while slow < len(flags) and goal != 'B':
        if fast == len(flags):
            fast = slow
            goal = 'G' if goal == 'R' else 'B'
            continue

        if flags[slow] == goal and flags[fast] == goal:
            slow, fast = slow+1, fast+1
            continue

        if flags[fast] != goal:
            fast += 1
            continue

        flags[slow], flags[fast] = flags[fast], flags[slow]
        slow, fast = slow+1, fast+1



'''                             Book Solution                            '''
def partition(arr):
    low, mid, high = 0, 0, len(arr)-1
    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

'''                             Test Cases                               '''



def main():
    test = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    dutch_flag(test)
    assert test == ['R', 'R', 'R', 'G', 'G', 'B', 'B']

    test2 = ['R', 'R', 'R']
    dutch_flag(test2)
    assert test2 == ['R', 'R', 'R']

    test3 = ['R', 'R', 'R', 'B', 'G']
    dutch_flag(test3)
    assert test3 == ['R', 'R', 'R', 'G', 'B']

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Note that you could make this process more modular by taking in a list of the ordering of the chars and solve the
        problem based on any arbitrary list of chars.
    * I like their idea of three partitions using three pointers where you know each partition will be correctly once you have
        passed over it. Work it out on paper and it makes a low of sense
    * Not that you do need the mid <= high because you can perform a swap that will make the high = mid and then that 
        value at mid still needs to be processed.
'''

