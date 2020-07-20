"""
Date: 7/19/20
8.1 Implement autocomplete system
"""

'''
Problem Statement: Implement an autocomplete system. That is, given a query string s and a set of all possible query
strings, return all strings in the set that have s as a prefix.
Example:
    query string: "de", set of strings ["dog", "deer", "deal"]
    returns ["deer", "deal"]

'''
from Trie import Trie
from Trie import ENDS_HERE
from typing import List

'''                             My Solution                              '''
def autocomplete(prefix: str, possible_queries: List[str]) -> List[str]:
    # Add all query strings to the Trie
    trie = Trie()
    for word in possible_queries:
        trie.insert(word)
    # Get the nested dictionary for input prefix
    prefix_dict = trie.find(prefix)
    # Get all words from this dictionary
    return complete_words(prefix, prefix_dict)

def complete_words(prefix, prefix_dict: dict):
    words = []
    for key, next_level in prefix_dict.items():
        if key == ENDS_HERE:
            words.append(prefix)
        else:
            words.extend(complete_words(prefix + key, next_level))
    return words


'''                             Book Solution                            '''
" They added a _elements(d) method to the Trie Class"
words = ["dog", "deer", "deal", "dealer", "dear"]
trie = Trie()
for word in words:
    trie.insert(word)

def autocomplete(s):
    suffixes = trie.find(s)
    return [s+w for w in suffixes]

'''                             Test Cases                               '''


def main():
    print(autocomplete("de", ["dog", "deer", "deal", "dealer", "dear"]))
    assert autocomplete("de", ["dog", "deer", "deal", "dealer", "dear"]) == ['deer', "deal", "dealer", "dear"]


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Comprehensions with recursive calls can get weird because they will return list of lists which is not always what you want
        and flattening them is just additional unnecessary work. Can use regular iteration with recursive calls and .extend()
    * Note from sourcery about their solution code. If you are doing if x then variable = blah blah blah else variable = blah blah blah
        that should not be broken down into two separate chunks it should be a single line expression
'''
