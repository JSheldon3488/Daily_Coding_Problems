"""
Date: 7/27/20
8.3: Find Maximum XOR of element pairs
"""

'''
Problem Statement: Given an array of integers, find the maximum XOR of any two elements.

No example given
'''

'''                             My Solution                              '''
""" I did not know where to start with this one. I assume they mean that if you bitwise XOR both ints together
when would you end up with the maximum value? How to do this with a trie.... No clue. Doing this with the standard
O(n^2) double for loop is easy but pretty inefficient."""
from typing import List
def max_XOR_element_pairs(nums: List[int]) -> int:
    max_seen = float('inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if (xor := nums[i]^nums[j]) > max_seen:
                max_seen = xor
    return max_seen

'''                             Book Solution                            '''
class Trie:
    def __init__(self, k):
        self._trie = {}
        self.size = k

    def insert(self, item):
        trie = self._trie

        for i in range(self.size, -1,-1):
            bit = bool(item & (1 << i))
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]

    def find_max_xor(self, item):
        trie = self._trie
        xor = 0
        for i in range(self.size,-1,-1):
            bit = boot(item & (1 << i))
            if (1-bit) in trie:
                xor |= (1<<i)
                trie = trie[1 - bit]
            else:
                trie = trie[bit]
        return xor

'''                             Test Cases                               '''
def main():
    return

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * 
'''

