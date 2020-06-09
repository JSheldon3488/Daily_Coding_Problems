"""
Date: 6/9/20
5.1: Implement an LRU Cache
"""

'''
Problem Statement: Implement a Least Recently Used Cache. The cache should be able to be initialized with cache size n,
and provide the following methods.
set(key,value): set key to value if there are already n items in the cache and we are adding a new item, also remove the LRU item.
get(key): get the value at key. if no such key exists return null.

Each operation should be O(1) runtime.

'''

'''                             Solution                              '''
class Node():
    """ Node class used for nodes in a linked list """
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next


class LinkedList():
    """ Linked List class used to implement LRU Cache priority (Least Recently Used at head to Most Recently Used at tail)
    Note: head and tail are dummy nodes that are never deleted """
    def __init__(self):
        """ Set up dummy head and tail to get the linked list started """
        self.head = Node(None, "head")
        self.tail = Node(None, "tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        """ Returns the first node of the linked list (not including head) """
        return self.head.next

    def get_tail(self):
        """ Returns the last node of the linked list (not including tail)"""
        return self.tail.prev

    def add(self, node):
        """ Inserts new node to the tail of the linked list """
        old_end = self.tail.prev
        old_end.next = node
        node.prev = old_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        """ removes node from the linked list """
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left


class LRU_Cache():
    """ Least Recently Used Cache """
    def __init__(self, n):
        self.max_size = n
        self.cache = {} # Cache of Nodes
        self.lru = LinkedList()

    def set(self, key, value):
        """ Set key to value in the cache. If there are already n items in the cache and we are adding a new item, than remove the LRU item from the cache.
         (key,value) -> Node -> Cache -> Update LRU List """
        n = Node(key,value)
        self.lru.add(n)
        self.cache[key] = n

        if len(self.cache) > self.max_size:
            # Remove LRU Node from LRU list and cache
            head = self.lru.get_head()
            self.lru.remove(head)
            del self.cache[head.key]

    def get(self, key):
        """ get the value at key. if no such key exists return null.
        key -> node -> update LRU list -> value """
        if key in self.cache:
            node = self.cache[key]
            # Move it up in LRU linked list
            self.lru.remove(node)
            self.lru.add(node)
            return node.val
        return None


'''                             Test Cases                               '''
def main():
    return

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * How do I keep track of LRU without some sort of sorted container?
        ** Can't. Need to use a linked list that keeps node in order from least recently used to most recently used
    * Why does our Node class need a key attribute?
        ** We need to be able to get the key so when we get a node off the LRU linked list we can use the key to delete
        that entry in the cache.
    * I think their use of dummy nodes for head and tail and then calling get_head and get_tail can add some confusion so make sure to comment well
    * I do not think there is a reason to do if key in dict: del dict[key] when adding a new item to the dict because only single key allowed in dictionary so it
    will delete and override the old value anyways
    * The interesting part of this problem is using multiple data structures together to improve efficiency. We use the linked list data structure to be able to keep
    an ordering on least recently used to most recently used. Usually we would have to search the Linked List to update it but here we do not need to because we are saving the nodes
    in our cache that can be accessed in O(1) time. We use the key to access the node in the cache and then can update the LRU list in O(1) time, as well as get the value for a given
    key in O(1) time because each node has a value associated with it. So combining the ideas of Nodes, Linked Lists, and Hash Tables we can solve an LRU cache in O(1) time.
'''

