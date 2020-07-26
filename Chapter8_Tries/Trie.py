ENDS_HERE = "#"


class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def find(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return None
        return trie

    def _elements(self,d):
        result = []
        for c,v in d.items():
            subresult = [''] if c == ENDS_HERE else [c+s for s in self._elements(v)]
            result.extend(subresult)
        return result
