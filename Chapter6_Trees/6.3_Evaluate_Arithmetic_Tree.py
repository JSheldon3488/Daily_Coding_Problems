"""
Date: 7/7/20
6.3: Evaluate Arithmetic Tree
"""
class Node():
    """ Node class used for making trees """
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

'''
Problem Statement: Suppose an arithmetic expression is given as a binary tree. each leaf is an integer and each internal node is one of +,-,*,/.
Given the root of such a tree, write a function to evaluate it.
Example:
            *
        +       +
     3     2 4     5
     Should return 45.
     (3+2) * (4+5)
     
     in-order: [3, +, 2, *, 4, +, 5]
     pre-order: [*, +, 3, 2, +, 4, 5]

'''

'''                             My Solution                              '''
def evaluate(root: Node) -> int:
    # Base Case:
    if isinstance(root.val, int):
        return root.val
    # Recursive Case:
    elif root.val == '*':
        return evaluate(root.left) * evaluate(root.right)
    elif root.val == '+':
        return evaluate(root.left) + evaluate(root.right)
    elif root.val == '-':
        return evaluate(root.left) - evaluate(root.right)
    else:
        try:
            result = evaluate(root.left)/evaluate(root.right)
            return result
        except ZeroDivisionError:
            return ZeroDivisionError



'''                             Book Solution                            '''
""" Same solution that I came up with. Note this is O(n) time and O(h) space complexity """


'''                             Test Cases                               '''
def main():
    assert evaluate(Node('*', left=Node('+', Node(3), Node(2)), right=Node('+', Node(4), Node(5)))) == 45
    assert evaluate(Node('*', left=Node('+', Node(3), Node(2)), right=Node('+', Node(4), Node(5)))) != 35
    assert evaluate(Node('/', left=Node('+', Node(3), Node(2)), right=Node('-', Node(5), Node(5)))) == ZeroDivisionError

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    *
'''

