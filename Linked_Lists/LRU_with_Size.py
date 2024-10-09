"""
LRU Cache with Size


# Time Complexity:
 - get() operation: O(1) - Hash map lookup and moving node to head are constant time.
 - put() operation: O(1) on average, but can be O(n) in worst case when multiple items need to be evicted.
   However, amortized time complexity is still O(1) as we don't evict items in every operation.

# Space Complexity:
- O(capacity) - The space used is proportional to the capacity of the cache.
  We store elements in both a hash map and a doubly linked list.
"""

class Node:
    def __init__(self, key, value, size):
        self.key = key
        self.value = value
        self.size = size
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum total size the cache can hold
        self.size = 0  # Current total size of elements in the cache
        self.cache = {}  # Hash map for O(1) lookup
        self.head = Node(0, 0, 0)  # Dummy head of doubly linked list
        self.tail = Node(0, 0, 0)  # Dummy tail of doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove an existing node from the linked list."""
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """Move a node to the head (mark as most recently used)."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Remove and return the tail node (least recently used)."""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key):
        """
        Get the value and size associated with the key if it exists in the cache.
        Also marks the key as most recently used.
        """
        node = self.cache.get(key)
        if not node:
            return None, None  # Key doesn't exist
        self._move_to_head(node)  # Mark as recently used
        return node.value, node.size

    def put(self, key, value, size):
        """
        Insert a key-value pair into the cache with the given size.
        If the key already exists, update its value and size.
        If inserting would exceed capacity, remove least recently used item(s).
        """
        node = self.cache.get(key)
        if node:
            # Key exists, update value and size
            self.size -= node.size
            node.value = value
            node.size = size
            self._move_to_head(node)
        else:
            # New key, create a new node
            new_node = Node(key, value, size)
            self.cache[key] = new_node
            self._add_node(new_node)

        self.size += size

        # Remove least recently used items if capacity is exceeded
        while self.size > self.capacity:
            tail = self._pop_tail()
            del self.cache[tail.key]
            self.size -= tail.size

# Test cases
def run_tests():
    print("Running test cases...")
    
    # Test case 1: Basic operations
    cache = LRUCache(10)
    cache.put("A", "Value A", 3)
    cache.put("B", "Value B", 5)
    print(cache.get("A"))  # Should print: ('Value A', 3)
    print(cache.get("B"))  # Should print: ('Value B', 5)
    
    # Test case 2: Exceeding capacity
    cache.put("C", "Value C", 4)  # This should evict "A"
    print(cache.get("A"))  # Should print: (None, None)
    print(cache.get("B"))  # Should print: ('Value B', 5)
    print(cache.get("C"))  # Should print: ('Value C', 4)
    
    # Test case 3: Updating existing key
    cache.put("B", "New Value B", 2)
    print(cache.get("B"))  # Should print: ('New Value B', 2)
    
    # Test case 4: Multiple evictions
    cache = LRUCache(10)
    cache.put("A", "Value A", 3)
    cache.put("B", "Value B", 3)
    cache.put("C", "Value C", 3)
    cache.put("D", "Value D", 3)  # This should evict "A"
    print(cache.get("A"))  # Should print: (None, None)
    print(cache.get("B"))  # Should print: ('Value B', 3)
    
    print("Test cases completed.")

# Run the test cases
run_tests()