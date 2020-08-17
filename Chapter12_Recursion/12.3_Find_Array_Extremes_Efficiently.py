"""
Date: 8/17/20
12.3: Find array extremes efficiently
"""

'''
Problem Statement: Given an array of numbers of length n, find both the min and max using less than 2*(n-2) comparisons.

'''

'''                             My Solution                              '''
""" Lets first look at how many 2*(n-2) is for different inputs.
n=2 0 comparisons... seems impossible.
n=3 2 comparisons
n=4 4 comparisons
n=5 6 comparisons
...
This feels like a merge sort type of problem but you only keep track of the min and max seen on each merge. Base case
would be when the length of the array is size 1 then that is min and max and can be returned with no comparison. When array
is size 2 need to do a single comparison to get min and max. When larger than size 2 need to compare solved subproblems
min and max to decide new min and max. The thing I am not remembering how to do is unwind and rewind back up a recursive
tree for merge sort type problems."""
from typing import List


def min_max(n: List) -> tuple:
    # Base Cases
    if len(n) == 1:
        return n[0], n[0]
    elif len(n) == 2:
        if n[0] <= n[1]:
            return n[0], n[1]
        else:
            return n[1], n[0]

    # Recursive Case
    else:
        middle = len(n) // 2
        min1, max1 = min_max(n[:middle])
        min2, max2 = min_max(n[middle:])
        minimum = min1 if min1 <= min2 else min2
        maximum = max1 if max1 >= max2 else max2
        return minimum, maximum


'''                             Book Solution                            '''
def min_and_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    elif len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    else:
        n = len(arr)//2
        lmin, lmax = min_and_max(arr[:n])
        rmin, rmax = min_and_max(arr[n:])
        return min(lmin,rmin), max(lmax,rmax)

'''                             Test Cases                               '''


def main():
    assert min_max([1, 2, 3]) == (1, 3)
    assert min_max([3, 2, 1]) == (1, 3)
    assert min_max([1, 2, 3, 4]) == (1, 4)
    assert min_max([1, 4, 3, 2]) == (1, 4)
    assert min_max([1, 2, 3, 4, 5]) == (1, 5)
    assert min_max([4, 5, 3, 1, 3]) == (1, 5)

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * The way I did the merge sort implementation was by setting up the base cases for the len 1 and 2 arrays and then
        for cases of n >= 3 doing two recursive calls on the left and right half of the array to get their min and max for each
        half and then return the result of comparing the two mins and the two maxes to get the min and max of the combined subarrays.
        This process will keep unwinding up the recursion tree until the entire problem is solved. The benefit in speed up is that at
        each layer you only need to compare the min to the min and the max to the max.
    * When comparing two elements can use min max built ins
    * We almost had the exact same solution as the book! Getting better
'''
