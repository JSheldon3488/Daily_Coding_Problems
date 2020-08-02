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
them quickly. The goal is to have the Huffman tree so that you can encode a string as a bit string for space efficiency and
then be able to decode it, therefore each path must be unique and when you get to a leaf you know that its over and can
return that character.
After a quick peek at the wiki page I think I know how this works so I will try to code it up."""

import heapq
from collections import defaultdict
from itertools import count
from typing import List


class Node:
    def __init__(self, char=None, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

    def __str__(self):
        return f'char: {self.char}, left_char: {self.left.char}, right_char: {self.right.char}'


def huffman_tree(frequencies: dict):
    counter = count()
    heap = []

    for char, freq in frequencies.items():
        heapq.heappush(heap, (freq, next(counter), Node(char=char, left=None, right=None)))

    # Pop off two min items off heap, combine, and put back on heap
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        combined = (f1 + f2, next(counter), Node(char=None, left=left, right=right))
        heapq.heappush(heap, combined)

    return heap[0][2]  # Just need tuples not heap list


def create_freq_map(words: List[str]) -> dict:
    freq_map = defaultdict(int)
    for word in words:
        for char in word:
            freq_map[char] += 1
    return freq_map


def my_encode(node: Node, encoding="", mappings=None):
    # Base Cases
    if mappings is None:
        mappings = {}
    if not node:
        return
    if not node.left and not node.right:
        mappings[node.char] = encoding

    # Recursive Cases
    my_encode(node.left, encoding + '0', mappings)
    my_encode(node.right, encoding + '1', mappings)
    return mappings


'''                             Book Solution                            '''


class Node_Book:
    def __init__(self, char, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right


def build_tree(frequencies):
    nodes = []
    for char, frequency in frequencies.items():
        heapq.heappush(nodes, (frequency, Node_Book(char)))

    while len(nodes) > 1:
        f1, n1 = heapq.heappop(nodes)
        f2, n2 = heapq.heappop(nodes)
        node = Node_Book('*', left=n1, right=n2)
        heapq.heappush(nodes, (f1 + f2, node))

    root = nodes[0][1]
    return root


def encode(root, string="", mapping=None):
    if mapping is None:
        mapping = {}

    if not root:
        return

    if not root.left and not root.right:
        mapping[root.char] = string

    encode(root.left, string + '0', mapping)
    encode(root.right, string + '1', mapping)

    return mapping


'''                             Test Cases                               '''


def main():
    # My Examples
    freq_map = create_freq_map(["cats", "bats", "ball", "test", "this", "he"])
    print(freq_map)

    huff_tree = huffman_tree(freq_map)
    print(sorted(freq_map, key=freq_map.get, reverse=True))
    print(my_encode(huff_tree))

    # Book Examples
    book_huff_tree = build_tree({'a': 3, 'c': 6, 'e': 8, 'f': 2})
    print(encode(huff_tree))
    print(encode(book_huff_tree))


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Inserting from worst (min freq) to best (max freq) like this ensures that the highest frequency items are at the top
        of the tree and have the shortest path.
    * How to set the key value for the heap? Use tuples and it will check in order of the tuple (The item must be hashable)
        * Also if two chars have the same frequency will have a problem so you should make the second item of the tuple
            a counter item for count insertion order. So you will store a three item tuple (freq, count, Node)
    * building a tree like this is nlogn time because each pop and push is logn
    * When recursively updating a structure like a dictionary you can pass that dictionary into the function and just start it
        with a default empty dict
    * Their implementation will fail if two characters have the same frequency
    * Their implementation of separating the frequencies from the Nodes is better than mine. They only add nodes as left
    and right not other tuples! Smart then can just return the last node and have a tree of nodes without all the frequency stuff
    * I really like their encode method as well.
'''
