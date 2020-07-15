"""
Date: 7/15/20
7.2: Convert Sorted Array to BST
"""
'''
Problem Statement: Given a sorted array, convert it to a height balanced BST.
Example: [1,2,3,4,5,6,7]
    Solution:   4
            2       6
          1   3   5   7
Example: [1,2,3,4,5,6]
    Solution:   4
            2       5
          1   3       6
'''

'''                             My Solution                              '''
from Chapter7_Binary_Search_Trees.BST import *

def array_to_BST(sorted):
    # Base Cases:
    if len(sorted) == 0:
        return None
    elif len(sorted) == 1:
        return Node(sorted[0])
    elif len(sorted) == 2:
        return Node(sorted[0], left=None, right=Node(sorted[1]))

    # Recursive Cases:
    middle_idx = len(sorted) // 2
    left = array_to_BST(sorted[:middle_idx])
    right = array_to_BST(sorted[middle_idx + 1:])
    return Node(sorted[middle_idx], left, right)


'''                             Book Solution                            '''
def make_bst(array):
    if not array:
        return None

    mid = len(array) // 2

    root = Node(array[mid])
    root.left = make_bst(array[:mid])
    root.right = make_bst(array[mid + 1:])

    return root


def main():
    # PrintTree function for checking results
    def printTree(node, level=0):
        if node != None:
            printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.data)
            printTree(node.right, level + 1)

    # Both algorithms produced the same result
    printTree(array_to_BST([1, 2, 3, 4, 5, 6, 7]))
    printTree(make_bst([1, 2, 3, 4, 5, 6, 7]))
    printTree(array_to_BST([1, 2, 3, 4, 5, 6]))
    printTree(make_bst([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Very confused on if they want us to return a Node Object that is a balanced BST or a BST object?
        ** If they just want a bst Object then you would use the same algorithm but instead create one BST Object
        and insert into it as you go.
    * They used the same algorithm as I did but just a cleaner version than me. I think I have a tendency to do this 
        same mistake where I overcomplicated the base case to be sure that I know what is happening in the smaller cases.
        I need to stop doing this and simplify my code and really break it down to its simplest form!
    * Good thought process but try to break the base cases down to their simplest form.
'''
