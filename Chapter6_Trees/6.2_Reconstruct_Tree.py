"""
Date: 6/18/20
6.1: Reconstruct tree from pre-order and in-order traversals
"""

'''
Problem Statement: Given a pre-order and in-order traversals of a binary tree, write a function to
reconstruct the tree. (You will be given both)

Example: [a,b,d,e,c,f,g] and [d,b,e,a,f,c,g]
        a
    b       c
  d   e   f   g
'''

'''                             My Solution                              '''
""" We will be given both so there must be a way to use the two pieces of information
to reconstruct the tree. We could solve for all the nodes in the left and right subtree
because we know the root from the pre-order and we know from the in-order how many nodes
will be in the left subtree. 
So I am thinking use the pre-order to get the root, then find this root in the in-order and slice
the list around that root. If the new list is length 3 we know how to construct it l,p,r.
If it is length 2 we know left, parent. If it is length 1 just single node.
The hard part might be if itis more than length 3. I think you can just recursively keep calling until
you get a length <= 3.
So the final idea is to use the pre-order to get the roots and slice up the in-order list into left and
right subtrees and then use in-order to reconstruct the slices if <= 3 otherwise use pre-order to get the next
root and slice again. Then glue back all these results at the end (potentially tricky)."""
from typing import List

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def reconstruct_tree(pre_order: List, in_order: List):
    if not pre_order or not in_order:
        return None

    root_val = pre_order[0]
    split = in_order.index(root_val)
    left_subtree, right_subtree = in_order[:split], in_order[split+1:]
    root = Node(root_val)
    if len(left_subtree) <= 3:
        root.left = reconstruct_helper(left_subtree)
    else:
        root.left = reconstruct_tree(pre_order[1:], left_subtree)
    if len(right_subtree) <= 3:
        root.right = reconstruct_helper(right_subtree)
    else:
        root.right = reconstruct_tree(pre_order[1:], right_subtree)

def reconstruct_helper(in_order: List):
    if len(in_order) == 1:
        return Node(in_order[0])
    if len(in_order) == 2:
        return Node(in_order[1], left= Node(in_order[0]))
    if len(in_order) == 3:
        return Node(in_order[1], left= Node(in_order[0]), right= Node(in_order[2]))


'''                             Book Solution                            '''
def reconstruct(preorder, inorder):
    if not preorder and not inorder:
        return None

    if len(preorder) == len(inorder) == 1:
        return Node(preorder[0])

    root = Node(preorder[0])
    root_index = inorder.index(preorder[0])
    root.left = reconstruct(preorder[1: 1+root_index], inorder[0:root_index])
    root.right = reconstruct(preorder[1+root_index:], inorder[root_index+1:])

    return root



'''                             Test Cases                               '''
def main():
    assert reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']) == \
        Node('a', left= Node('b', left=Node('d'), right=Node('e')), right= Node('c', left=Node('f'), right=Node('g')))


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * To find the index of a given element in a List in Python use .index()
    * Try to use the simplest algorithm possible the first time you do something and only make it more
        complex if you need to
    * The thing that I missed is that the in order index can also be used to slice up the pre-order tree
        for the next level of recursion.
'''

