"""
Date: 7/10/20
6.4: Get tree level with minimum sum
"""

'''
Problem Statement: Given a binary tree, return the level of the tree that has the minimum sum. The level of a node
is defined as the number of connections required to get to the root, with the root having level zero.
Example:
            1
        2       3
             4     5
        Solution: level 0 (sum is 1 at level 0, 5 at level 2, and 9 at level 3)
'''

class Node():
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''                             My Solution                              '''
def min_sum_level(root: Node) -> int:
    if not root:
        return 0

    # Variable Setup
    min_level, min_seen = 0, root.val
    level, level_nodes = 0, [root]

    # Find min level
    while level_nodes:
        # Calculate this levels sum and compare it to min_seen
        level_sum = sum(node.val for node in level_nodes)
        if level_sum < min_seen:
            min_seen = level_sum
            min_level = level
        # Reset level_nodes and level for next level
        level_nodes = [node.left for node in level_nodes if node.left != None] + [node.right for node in level_nodes if node.right != None]
        level += 1

    return min_level

'''                             Book Solution                            '''
from collections import defaultdict, deque

def smallest_level(root):
    queue = deque([])
    queue.append((root,0))
    level_to_sum = defaultdict(int)

    while queue:
        node,level = queue.popleft()
        level_to_sum[level] += node.val
        if node.right:
            queue.append((node.right,level+1))
        if node.left:
            queue.append((node.left,level+1))

    return min(level_to_sum, key=level_to_sum.get)

'''                             Test Cases                               '''
def main():
    assert min_sum_level(Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))) == 0
    assert min_sum_level(Node(10, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))) == 1
    assert min_sum_level(Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(-5)))) == 2
    assert min_sum_level(Node(1)) == 0

    assert smallest_level(Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))) == 0
    assert smallest_level(Node(10, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))) == 1
    assert smallest_level(Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(-5)))) == 2
    assert smallest_level(Node(1)) == 0

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * I feel like the two list comprehensions are easy to read but potentially slow because you are iterating over the container twice.
        This could be done with a single iteration over the container and some conditionals but it will make the code more complex
    * This could also be solved with a recursive helper function but this just felt easy enough to solve with forward iteration
    * a list of None's will still pass the while loop conditional check (can fix this by filtering out Nones in the while loop but that is expensive especially later in the tree)
        ** The first pass is redundant in the solution above but its a single node so not expensive and then the code is much easier to read 
    * My solution is O(n) but it is 3n because i iterate over the same node 3 times. (once for sum, once for left and once to get right)
        ** Using a dictionary and queue solves this problem because then you only have to touch each node once to update the queue and dictionary at each node
        ** always think about using a queue and a dictionary when you just want to process an item once but may need to process children of that item as well
    * Inside the sum function you do not need to use [] for the list comp explicitly
'''

