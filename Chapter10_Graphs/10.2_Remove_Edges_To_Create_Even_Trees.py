"""
Date: 8/4/20
10.2: Remove Edges to Create Even Trees
"""

'''
Problem Statement: You are given a tree with an even number of nodes. Consider each connection between a parent and child
node to be an "edge". You would like to remove some of these edges, such that the disconnected subtrees that remain each
have an even number of nodes.
    Example:
            1
        2       3
              4   5
           6  7  8
In this case, if we remove the edge (3,4) both resulting subtrees will be even. 

Write a function that returns the maximum number of edges you can remove while still satisfying this requirement.

'''

'''                             My Solution                              '''
""" The first though that comes to mind would be getting to subtrees of size 2 but I think all nodes must still be present
in the final solution and if you look at node 4 there is no reason to get to a subtree of size two, deleting any of 4s edges does
not help you. Second thought that comes to mind is this problem could be better defined. Can we just leave nodes by themselves? If
not what happens of we are given a tree with 3 nodes a root,left,right. If we can not leave a node alone then this is impossible.
Based on my misunderstanding of the problem I am going to look at the solution and come back later and solve it. Also I guess
stating that it is a tree means it is a directed graph with no cycles and only one way directions down."""
from typing import List, Dict

def count_descendents(key, graph: Dict[int, List[int]]) -> int:
    if len(graph[key]) == 0:
        return 0
    return len(graph[key]) + sum(count_descendents(desc, graph) for desc in graph[key])

def count_removable_edges(graph: Dict[int, List[int]]) -> int:
    descendents_counts = {}
    for key in graph:
        descendents_counts[key] = count_descendents(key, graph)
    return sum(1 for node in descendents_counts if descendents_counts[node] % 2 != 0)-1


'''                             Book Solution                            '''
""" If a node has an odd number of descendents we can cut off that node from its parent and have an even subtree. I beleive
we want to start with the lowest node possible and work are way up. Each node that has an odd number of descendents (besides the root)
will count towards the edges we need to cut. Note that we do not actually need to do the cutting and reshapping of the data structure just
count what we could remove. We need to transcend the tree and store a number for how many descendents each node as and once we do
this we can simply count the number of odd values and get our answer."""

from collections import defaultdict

def traverse(graph, curr, result):
    descendents = 0
    for child in graph[curr]:
        num_nodes, result = traverse(graph, child, result)
        result[child] += num_nodes-1
        descendents += num_nodes
    return descendents+1, result

def max_edges(graph):
    start = list(graph)[0]
    vertices = defaultdict(int)
    _, descendents = traverse(graph, start, vertices)
    return len([val for val in descendents.values() if val % 2 == 1])

'''                             Test Cases                               '''


def main():
    graph = {1: [2, 3],
             2: [],
             3: [4, 5],
             4: [6, 7, 8],
             5: [],
             6: [],
             7: [],
             8: []
             }
    assert count_removable_edges(graph) == 2

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * I think the biggest take away from this problem is how important it is to define your problem correctly.
    * Also practice DFS a lot so that it comes to you naturally
    * Their solution is a little more complex but has the benefit of only traversing the tree once
'''
