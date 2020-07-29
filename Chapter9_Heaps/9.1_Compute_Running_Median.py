"""
Date: 7/29/20
9.1: Compute the Running Median
"""

'''
Problem Statement: Compute the running median of a sequence of numbers. That is given a stream of numbers, print out the median
of the list so far after each new element. Recall that the median of an even number list is the average of the two middle elements.
Example:
    [2,1,5,7,2,0,5]
    :prints 2, 1.5, 2, 3.5, 2, 2, 2
'''
import heapq
from typing import List
'''                             My Solution                              '''
''' I am not sure why we would want to use a heap here. Heaps are not sorted so they do not help in that regard. Unless we
pop everything off each time to create a sorted list after each insertion but that seems really inefficient. Not really sure what
a heap helps us with here. The book says if we use two heaps, a min heap and a max heap and we keep all elements smaller than the previous
median in the max heap, and all elements larger then the median in the min heap, and we keep these heaps the same size then
we are guaranteed that the median is either the root of the min or max heap or both. With this information and some work
on the white board I wrote the solution below'''
def running_median(nums: List[int]) -> None:
    """ Takes in a list of ints and prints out a running median as if you were iterating over the list one by one """
    # Initialize variables
    max_heap = [] # Everything is multiplied by -1 to get a max heap
    min_heap = [nums[0]]
    median = nums[0]
    print(median)

    # Median printing loop
    for num in nums[1:]:
        # Insert into correct heap
        if num > median:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -1*num)

        # Keep balance invariant
        if len(min_heap) - len(max_heap) > 1:
            move = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -1*move)
        elif len(max_heap) - len(min_heap) > 1:
            move = -1*heapq.heappop(max_heap)
            heapq.heappush(min_heap, move)

        # Print and overwrite median
        if len(min_heap) > len(max_heap):
            median = min_heap[0]
        elif len(max_heap) > len(min_heap):
            median = -1*max_heap[0]
        else:
            median = (min_heap[0] + -1*max_heap[0])/2
        print(median)

'''                             Book Solution                            '''
def get_median(min_heap, max_heap):
    if len(min_heap) > len(max_heap):
        min_val = heapq.heappop(min_heap)
        heapq.heappush(min_heap, min_val)
        return min_val
    elif len(min_heap) < len(max_heap):
        max_val = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_val)
        return max_val
    else:
        min_val = heapq.heappop(min_heap)
        heapq.heappush(min_heap, min_val)
        max_val = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_val)
        return (min_val + max_val) / 2


def add(num, min_heap, max_heap):
    if len(min_heap) + len(max_heap) <= 1:
        heapq.heappush(max_heap, num)
        return

    median = get_median(min_heap, max_heap)
    if num > median:
        heapq.heappush(min_heap,num)
    else:
        heapq.heappush(max_heap, num)


def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, root)
    elif len(max_heap) > len(min_heap) + 1:
        root = heapq.heappop(max_heap)
        heapq.heappush(min_heap, root)

def print_median(min_heap, max_heap):
    print(get_median(min_heap,max_heap))

def running_median_book(stream):
    min_heap = []
    max_heap = []
    for num in stream:
        add(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        print_median(min_heap, max_heap)

'''                             Test Cases                               '''
def main():
    running_median([2,1,5,7,2,0,5])
    print()
    running_median_book([2,1,5,7,2,0,5])
if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * heapq documentation on docs.python.ord are great!
    * to implement a max heap just multiply by -1 on insertions and retrievals 
    * If you are really confused on a problem try to think how you can combine multiple data structures to implement a solution
    * Always refactor and modularize your code
    * Book solution has a bug because they did not do the *-1 to convert a heap from min to max heap.
'''

