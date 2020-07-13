"""
Date: 7/11/20
7.1: Find floor and ceiling
"""
from Chapter7_Binary_Search_Trees.BST import BST, Node

'''
Problem Statement: Given a binary search tree, find the floor and ceiling of a given integer.
The floor is the highest element in the tree less than or equal to an integer, while the
ceiling is the lowest element in the tree greater than or equal to an integer.
If either value does not exist, return None.
Example: input 4 tree below
            7
        5     10
    -1    6      25
    Returns: floor = -1, ceiling = 5
'''

'''                             My Solution                              '''
def floor_ceiling(input: int, root: Node, parent=None):
    # At Leaf case
    if not root:
        return (None, parent.data) if parent is not None else (None, None)

    # Equivalent Node Case
    elif root.data == input:
        return (root.data, parent.data) if parent is not None else (root.data, None)

    # In between node and parent case
    elif parent is not None and (root.data < input < parent.data):
        return root.data, parent.data

    # Need to recurse into deeper in tree case
    elif input < root.data:
        return floor_ceiling(input, root.left, root)
    else:
        return floor_ceiling(input, root.right, root)


'''                             Book Solution                            '''
def get_bounds(x, root, floor=None, ceil=None):
    if not root:
        return floor, ceil

    if x == root.data:
        return x,x

    elif x < root.data:
        floor,ceil = get_bounds(x, root.left, floor, root.data)
    elif x > root.data:
        floor,ceil = get_bounds(x, root.right, root.data, ceil)

    return floor,ceil

'''                             Test Cases                               '''


def main():
    bst = BST()
    bst.insert(7), bst.insert(5), bst.insert(10), bst.insert(-1), bst.insert(6), bst.insert(25)
    assert get_bounds(4, bst.root) == (-1,5)
    assert get_bounds(-2, bst.root) == (None, -1)
    assert get_bounds(6, bst.root) == (6,6)
    assert get_bounds(15, bst.root) == (25,10)
    assert get_bounds(7, bst.root) == (7, None)
    assert get_bounds(9,bst.root) == (None,10)


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * This problem was poorly described by the book. I thought they meant floor as in the node that would be below
        where the current node would go in a balanced search tree and ceiling was the node above. They just meant
        what two values are we between with the floor being the smaller one and the ceiling being the larger.
    * When doing recursion to keep track of some data you can use default None parameters to help you out
'''
