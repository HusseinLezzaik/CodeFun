"""
lru cache: https://leetcode.com/problems/lru-cache/description/

A Least Recently Used (LRU) Cache organizes items in order of use, allowing you to quickly identify which item hasn't been used for the longest amount of time.
Picture a clothes rack, where clothes are always hung up on one side. To find the least-recently used item, look at the item on the other end of the rack.

Under the hood, an LRU cache is often implemented by pairing a doubly linked list with a dictionary. (**)

Strengths:
- Super fast accesses. LRU caches store items in order from most-recently used to least-recently used. That means both can be accessed in O(1) time.
- Super fast updates. Each time an item is accessed, updating the cache takes O(1) time.

Weaknesses:
- Space heavy. An LRU cache tracking n items requires a linked list of length n, and a dictionary holding n items. That's O(n) space, but it's still two data structures (as opposed to one).

"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key to Node
        # Initialize the dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Remove node from linked list
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        # Always add to the front (right after head)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)  # Move to front as it's recently used
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove least recently used from cache and linked list
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

# Test Cases:
cache = LRUCache(2)
print(cache.put(1, 1))  # cache is {1=1}
print(cache.put(2, 2))  # cache is {1=1, 2=2}
print(cache.get(1))     # returns 1, cache is {2=2, 1=1}
print(cache.put(3, 3))  # evicts key 2, cache is {1=1, 3=3}
print(cache.get(2))     # returns -1 (not found)
print(cache.put(4, 4))  # evicts key 1, cache is {3=3, 4=4}
print(cache.get(1))     # returns -1 (not found)
print(cache.get(3))     # returns 3
print(cache.get(4))     # returns 4
