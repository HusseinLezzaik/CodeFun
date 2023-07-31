class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

"""
The MyQueue class uses a doubly linked list to implement a queue. All the operations (push, pop, peek, and empty) have a time complexity of O(1). Here's why:
- push: This operation just adds a new node to the front of the list, which involves a constant amount of work (creating a new node, updating the prev pointer of the old head, and updating the head pointer). So its time complexity is O(1).
- pop: This operation removes the node at the tail of the list, which also involves a constant amount of work (saving the value to return, updating the tail pointer, and updating the next pointer of the new tail). So its time complexity is O(1).
- peek: This operation just returns the value at the tail of the list, which is a constant time operation. So its time complexity is O(1).
- empty: This operation just checks whether the head pointer is None, which is a constant time operation. So its time complexity is O(1).

The space complexity of the MyQueue class is O(n), where n is the number of elements in the queue.
This is because it uses a doubly linked list to store the elements of the queue.
Each node in the list uses a constant amount of space, so the total space complexity is proportional to the number of elements in the queue.

"""
class MyQueue:

    def __init__(self):
        self.head = self.tail = None

    def push(self, x: int) -> None:
        if not self.head:
            self.head = self.tail = Node(x)
        else:
            new_node = Node(x, None, self.head)
            self.head.prev = new_node
            self.head = new_node

    def pop(self) -> int:
        if self.empty():
            return -1
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.tail.value

    def empty(self) -> bool:
        return not self.head


# Now let's test our queue
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # returns 1
print(q.pop())   # returns 1
print(q.empty()) # returns False
print(q.pop())   # returns 2
print(q.empty()) # returns True
