class Node:
    """ Node class used for nodes in a Tree """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

class BST:
    """ Simple Binary Search Tree Implementation
    Note: this is not a balanced binary search tree so does not guarantee log(n) operations
    """
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root:
            return "Empty Tree"
        else:
            return self.print_tree(self.root)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.print_tree(node.right, level + 1)

    def insert(self, x):
        if not self.root:
            self.root = Node(x)
        else:
            self._insert(x, self.root)

    def _insert(self, x, root):
        if x < root.data:
            if not root.left:
                root.left = Node(x)
            else:
                self._insert(x, root.left)
        else:
            if not root.right:
                root.right = Node(x)
            else:
                self._insert(x, root.right)

    def find(self, x):
        if not self.root:
            return False
        else:
            return self._find(x, self.root)

    def _find(self, x, root):
        if not root:
            return False
        elif x == root.data:
            return True
        elif x < root.data:
            return self._find(x, root.left)
        else:
            return self._find(x, root.right)