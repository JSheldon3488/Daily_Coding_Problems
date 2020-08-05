"""
Date: 8/3/20
10.1: Determine if a cycle exists
"""

'''
Problem Statement: Given an undirected graph, determine if it contains a cycle.

'''

'''                             My Solution                              '''
""" First we know the graph is undirected so it could have a cycle of two nodes that point to each other.
The way to solve this for all nodes would be start at node A, traverse to all his children and children's children,
and so forth until you either run out of nodes to visit or you have returned to A. I think breadth first search would be
more efficient so that you can end early on any small cycles. I am going to use dictionaries to map Nodes to its connecting nodes"""
from collections import deque
from typing import List, Dict


def detect_cycle(graph: Dict[str, List[str]]) -> bool:
    bfs = deque()

    for item in graph:
        start = item
        visited = [start]
        bfs.extend(graph[start])
        while bfs:
            node = bfs.popleft()
            if node == start:
                print(f'Cycle found starting with Vertex {start}')
                return True
            elif node not in visited:
                bfs.extend(graph[node])
                visited.append(node)

    return False


'''                             Book Solution                            '''
def search(graph, vertex, visited, parent):
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if search(graph, neighbor,  visited, vertex):
                return True
        elif parent != neighbor:
            return True

    return False

def has_cycle(graph):
    visited = {v: False for v in graph.keys()}

    for vertex in graph.keys():
        if not visited[vertex]:
            if search(graph, vertex, visited, parent=None):
                return True

    return False

'''                             Test Cases                               '''


def main():
    # My Solution Cases
    graph = {'JFK': ['LAX', 'SFO'], 'SFO': ['ORL'], 'ORL': ['JFK', 'LAX', 'DFW'], 'LAX': ['DFW'], 'DFW': []}
    graph2 = {'SFO': ['ORL'], 'ORL': ['JFK', 'LAX', 'DFW'], 'LAX': ['DFW'], 'JFK': ['LAX', 'SFO'], 'DFW': []}
    graph3 = {'DFW': [], 'ORL': ['JFK', 'LAX', 'DFW'], 'LAX': ['DFW'], 'JFK': ['LAX', 'SFO'], 'DFW': [], 'SFO': ['ORL']}
    graph4 = {'LAX': ['DFW'], 'ORL': ['DFW'], 'DFW': []}

    assert detect_cycle(graph) == True
    assert detect_cycle(graph2) == True
    assert detect_cycle(graph3) == True
    assert detect_cycle(graph4) == False


    # Their Solution Cases
    graph = {'LAX': ['DFW'], 'ORL': ['DFW'], 'DFW': []}
    assert has_cycle(graph) == False

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Always make sure to test different combinations of the same input to make sure your algorithm works. Especially in cases
        like this where not all data is seen.
    * Visited list is necessary here because if we did not have it and you had a node that mapped to a cycle you would be stuck
        in an infinite loop
    * using in for a list could get very expensive if the graph is very large. Dictionary better
    * Their algorithm is wrong although it does appear to be similar to ones I am seeing online so maybe I am misunderstanding 
        what a cycle is.
        ** I did solve the wrong problem I solved the problem as if it was a directed graph. Their solution makes sense
        with undirected graph
'''
