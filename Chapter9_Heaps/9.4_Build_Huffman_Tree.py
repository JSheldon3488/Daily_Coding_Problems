"""
Date: 8/1/20
9.4: Build a Huffman tree
"""

'''
Problem Statement: Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a
variable-length binary string such as 0101 or 11110, where shorter lengths correspond to more common letters. To accomplish
this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing
the path, descending to a left child corresponds to a 0 in the prefix, and going right corresponds to a 1.
Example Tree:
                null
            0           1
        0       1a  0t      1
    0c                          1s
encoding for "cats" = 0000110111

Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between characters and their
encoded binary strings.

'''

'''                             My Solution                              '''
""" The first thing that seems necessary is to build a max heap out of the frequency dictionary so that we can pop them off
the heap quickly as most frequent to least frequent and place them into the tree. I do not really remember how Huffman trees
work but I do remember something about the most frequent characters should have the shortest path so that you can get to
them quickly."""


'''                             Book Solution                            '''


'''                             Test Cases                               '''
def main():
    return

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    *
'''

