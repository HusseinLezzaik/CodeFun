class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

"""
# Time Complexity
- push: O(1) because we just add a node at the beginning of the linked list.
- pop: O(1) because we just remove a node from the beginning of the linked list.
- peek: O(1) because we just return the value of the head node of the linked list.
- is_empty: O(1) because we just check if the head of the linked list is None.

# Space Complexity
O(1) for each operation (push, pop, peek, is_empty) because we don't use any additional space that scales with the size of the input.
"""

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        return self.head.data if self.head is not None else None

    def is_empty(self):
        return self.head is None

# Let's test our Stack implementation
stack = Stack()

# The stack should be empty at this point
assert stack.is_empty() == True

# Let's add some items to the stack
stack.push('apple')
stack.push('banana')
stack.push('cherry')

# Now the stack should not be empty
assert stack.is_empty() == False

# The top of the stack should be 'cherry'
assert stack.peek() == 'cherry'

# Let's remove an item from the stack
assert stack.pop() == 'cherry'

# Now the top of the stack should be 'banana'
assert stack.peek() == 'banana'

# Let's remove all items from the stack
assert stack.pop() == 'banana'
assert stack.pop() == 'apple'

# The stack should be empty again at this point
assert stack.is_empty() == True