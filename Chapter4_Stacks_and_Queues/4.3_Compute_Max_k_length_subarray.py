"""
Date: 6/5/20
4.3: Compute maximum of k-length subarrays
"""

'''
Problem Statement: Given an array of ints and a number k, where 1<= k < array length, compute the max values of each subarray
of length k.
Example:
    [10,5,2,7,8,7] k = 3 Returns [10,7,8,8] (so basically the max of a subarray window of size k of each possible subarray window
    
Solve this is O(n) time and O(k) space.

'''

'''                             My Solution                              '''
from typing import List
from collections import deque

""" This first solution is O(n*k) because for each element in the list you have to find the max of a subarray of length k. There is a faster way."""
def max_of_subarray(k: int, nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)-(k-1)):
        result.append(max(nums[i:i+k]))
    return result

'''                             Book Solution                            '''
def max_of_subarray_faster(k: int, nums: List[int]) -> List[int]:
    result = []
    q = deque()
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)

    # Loop invariant: q is a list of indices where their corresponding values are in descending order
    for i in range(k,len(nums)):
        result.append(nums[q[0]])
        while q and q[0] <- i-k:
            q.popleft()
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    result.append(q[0])
    return result


'''                             Test Cases                               '''
def main():
    assert max_of_subarray(3, [10,5,2,7,8,7]) == [10,7,8,8]

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * I do not think the added complexity of their solution is worth the increase in speed or reduction in space.
'''

