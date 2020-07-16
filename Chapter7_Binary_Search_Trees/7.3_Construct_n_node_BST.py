"""
Date: 7/16/20
7.3: Construct all BSTs with n nodes
"""

'''
Problem Statement: Given an integer n, construct all possible binary search trees with n nodes where all values from
[1, ..., n] are used.
Example: n = 3
    Solution  1             1           2          3        3
                2             3       1   3      1         2
                  3         2                      2      1

As you can see this is a pretty tricky problem and you have to make sure that the BST property is not broken.
Smaller values must always be to the left and larger values always to the right.
'''

'''                             My Solution                              '''
from Chapter7_Binary_Search_Trees.BST import *
from itertools import permutations


def all_possible_binary_trees(n):
    data = [x for x in range(1, n + 1)]
    all_bst = []

    # Iterate over all values in the data creating all possible BST starting with that value as root. If you have all
    # permutations of the remaining data you can insert them into a tree and get all possible bst starting with that root.
    for index, value in enumerate(data):
        remaining_data = data[:index] + data[index+1:]
        all_insertion_orders = list(permutations(remaining_data))
        for insertion_order in all_insertion_orders:
            bst = BST()
            bst.insert(value)
            for val in insertion_order:
                bst.insert(val)
            all_bst.append(bst)

    return all_bst


'''                             Book Solution                            '''
def make_trees(low,high):
    trees = []

    if low > high:
        trees.append(None)
        return trees

    for i in range(low,high+1):
        left = make_trees(low, i-1)
        right = make_trees(i+1, high)

        for l in left:
            for r in right:
                node = Node(i, left = l, right = r)
                trees.append(node)

    return trees


'''                             Test Cases                               '''
def main():
    test = all_possible_binary_trees(3)
    for tree in test:
        tree.print_tree(tree.root)
        print(); print()

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * My solution works but I did not take into account that the middle node with 2 at root and [1,3] and [3,1] would make
        the same tree so I end up with duplicates.
    * Also note that some solutions are really hard to test! It is difficult to write a test case to check for
        the correct answer here
    * Book solution is weird because they said given n, not low to high. But in principal I get what they are doing and why
        it works.
    * They solved the problem using recursion and subtrees and I solved it using permutations because that is the first thing
        that came to my mind coming from statistics. Remember to always thing about trees in terms of recursion and subproblems.
'''
