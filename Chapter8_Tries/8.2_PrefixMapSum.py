"""
Date: 7/26/20
8.2: Create PrefixMapSum Class
"""

'''
Problem Statement:
Implement a PrefixMapSum class with the following methods:
    def insert(key: str, value: int) Set a given key's value in the map. If the key already exists overwrite the value.
    def sum(prefix: str) Return the sum of all values of keys that begin with a given prefix.

Example:
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3
    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5
'''

from Trie import Trie, ENDS_HERE
from collections import defaultdict
'''                             My Solution                              '''
class PrefixMapSum:
    def __init__(self):
        self._trie = Trie()
        self.values = defaultdict(int)

    def insert(self, key: str, value: int):
        self._trie.insert(key)
        self.values[key] = value

    def sum(self, prefix: sum):
        # Get all possible words with prefix
        words = self.complete_words(prefix, self._trie.find(prefix))
        # Sum values from values dictionary for all possible words
        return sum(self.values[word] for word in words)

    def complete_words(self, prefix, prefix_dict: dict):
        words = []
        for key, next_level in prefix_dict.items():
            if key == ENDS_HERE:
                words.append(prefix)
            else:
                words.extend(self.complete_words(prefix + key, next_level))
        return words

'''                             Book Solution                            '''


'''                             Test Cases                               '''
def main():
    mapsum = PrefixMapSum()
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3
    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Using key.startswith(prefix) would allow us to do this without even using a trie and would make insertions fast
        but would do poorly with summation because it will check every single key in the dictionary
    *
'''

