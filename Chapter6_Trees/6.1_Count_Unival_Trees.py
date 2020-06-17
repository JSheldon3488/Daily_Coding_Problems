"""
Date: 6/15/20
6.1: Count unival trees
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

'''
Problem Statement: A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
Note: A leaf counts as a unival subtree.

Example: [0,1,0,1,1,1,0] (pre order traversal)
          0
       1     0
           1   0
         1   1
    solution: 5
'''

'''                             My Solution                              '''
""" If a nodes subtrees are unival trees and both its subtrees have the same data and match this nodes data
then this node is also a unival subtree. That is the logic you have to ask to solve this
problem. For each node you need to know if its subtrees are unival and if they have the same
data as the current node. If you start at the leaves and work your way up the tree this can be solved in
O(n) time. """


def count_unival_subtrees(root: Node) -> int:
    count, _ = unival_helper(root)
    return count

def unival_helper(node: Node):
    # Base Case: Empty Node is unival but doesnt add to count
    if not node:
        return 0, True

    # Recursive Case: Go to leaves first and work way back up
    # At node find out left and right subtree count and if they are unival subtrees.
    left_count, left_is_unival = unival_helper(node.left)
    right_count, right_is_unival = unival_helper(node.right)
    total_count = left_count + right_count

    # Evaluate if this node is a unival subtree or not
    if left_is_unival and right_is_unival:
        if node.left and node.left.data != node.data:
            return total_count, False
        if node.right and node.right.data != node.data:
            return total_count, False
        return 1+total_count, True

    return total_count, False



'''                             Test Cases                               '''
def main():
    root = Node(0, left=Node(1), right= Node(0, left=Node(1, left=Node(1), right=Node(1)), right=Node(0)))
    print(count_unival_subtrees(root))
    assert count_unival_subtrees(root) == 5

    root = Node('a', left=Node('a'), right= Node('a', left=Node('a'), right=Node('a', left = None, right = Node('b'))))
    print(count_unival_subtrees(root))
    assert(count_unival_subtrees(root)) == 3

    root = Node('a', left=Node('c'), right= Node('b', left=Node('b'), right=Node('b', left = None, right = Node('b'))))
    print(count_unival_subtrees(root))
    assert(count_unival_subtrees(root)) == 5



if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Sometimes it is better to recurse to the bottom of the tree and propogate back up the results as you go
        to solve a problem more efficiently.
    * To recurse to the leavs of a tree just call on left and right at the start of the recursive case and
        have the code logic below that. In other words do the recursive calls first then when they return
        results use those afterwards to evaluate this node.
'''

