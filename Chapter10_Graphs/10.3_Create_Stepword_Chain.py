"""
Date: 8/6/20
10.3: Create stepword chain
"""

'''
Problem Statement: Given a start word, and end word, and a dictionary of valid words, find the shortest transformation 
sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed
word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary has the same
length as start and end and is lowercase.
Example 1:
    start = "dog"
    end = "cat"
    words = ["dot", "dop", "dat", "cat"]
        :returns ["dog", "dot", "dat", "cat"]
        ** Notice we put the start word in the list
                
Example 2:
    start = "dog"
    end = "cat"
    words = ["dot", "tod", "dat", "dar"]
        :returns Null
        ** So the end word must actually be in the list of valid words 

'''

'''                             My Solution                              '''
""" Right away this jumps out to me as a breadth first search graph problem where we have to build up the graph
ourselves and then do BFS on it to see if we get to a solution. I don't know why the start work is not in the valid words
but I think it will have to be in our graph. I am going to use a dictionary to map a node to a list of its possible neighbors
where each neighbor can only have one letter difference from the node. For the BFS algorithm we are going to need a visited
list so that we do not get stuck in a cycle. We are also going to need some way to pass forward potential answers so that
if we get to the correct solution we can return the answer. The more I thought about it I think DFS might be easier. I think
both are possible but BFS seems a little tricky because you need to keep track of results list without the help of recursive
calls. Could use a tuple of (word, results)."""
from typing import List, Dict
from _collections import deque, defaultdict

def single_letter_diff(a: str, b: str) -> bool:
    """ Returns true if the two words only have one letter different otherwise false"""
    diff = sum(1 for i in range(len(a)) if abs(ord(a[i]) - ord(b[i])) > 0)
    return diff == 1

def build_graph(words: List[str]) -> Dict:
    """ Tokes all the words in a list and creates a undirected graph for each word where each graph connection is
    based on if that word and the connected word only differ by one letter.
    Graph is represented with a dictionary Node -> List connected Nodes """
    # Setup graph
    graph = {}
    for word in words:
        graph[word] = []

    # Add all graph connections
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if single_letter_diff(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])

    return graph

def path_finder_dfs(start: str, end: str, graph: Dict, visited=defaultdict(int), result=[]):
    # Base Case
    if not graph[start] or visited[start]:
        return None
    if start == end:
        return result+[end]

    # Recursive Case
    visited[start] = True
    for word in graph[start]:
        if path := path_finder_dfs(word, end, graph, visited, result+[start]):
            return path

def path_finder_bfs(start: str, end: str, graph: Dict):
    # Setup
    visited = defaultdict(int)
    visited[start] = True
    deck = deque()
    for word in graph[start]:
        deck.append((word, [start]))

    # Solve for path
    while deck:
        word, result = deck.popleft()
        # Found path
        if word == end:
            return result + [end]
        # Still Searching
        for next_word in graph[word]:
            if not visited[next_word]:
                deck.append((next_word, result+[word]))
        visited[word] = True
    # No path found
    return None

def find_path(start: str, end: str, words: List[str]) -> List[str]:
    graph = build_graph(words+[start])
    # return path_finder_bfs(start, end, graph)
    return path_finder_dfs(start, end, graph)


'''                             Book Solution                            '''
from string import ascii_lowercase

def word_ladder(start, end, words):
    queue = deque([(start, [start])])

    while queue:
        word, path = queue.popleft()
        if word == end:
            return path

        for i in range(len(word)):
            for char in ascii_lowercase:
                next_word = word[:i] + char + word[i+1:]
                if next_word in words:
                    words.remove(next_word)
                    queue.append([next_word, path+[next_word]])

    return None

'''                             Test Cases                               '''
def main():
    start, end = "dog", "cat"
    words = ["dot", "dop", "dat", "cat"]
    print(path := find_path(start, end, words))
    expected = ['dog', 'dot', 'dat', 'cat']
    assert path == expected

    start, end = "dog", "cat"
    words = ["dot", "tod", "dat", "dar"]
    print(find_path(start, end, words))
    assert find_path(start, end, words) is None


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Using the word dictionary to describe a list of words in Python is extremely sloppy. Do not do this!
    * I feel like using a list for keeping track of visited nodes is bad and a dictionary would be much more efficient
        because then we do not have to use the O(n) call to `in`
    * Both DFS and BFS work the trick is knowing how to pass the data forward to the next level. For DFS its easy with recursive
    calls, for BFS its a little harder but storing tuples of data (word, results_list) worked.
    * So their solution changes each letter in the word 26 times from a to z then checks if that word is in the list
        or words and if it is removes it and adds it to the queue... this seems bad. Also not really in the spirit of
        creating a graph and using a graph data structure to solve the problem. This is just BFS with a really inefficient
        way to check if two words are off by a single letter.
'''

