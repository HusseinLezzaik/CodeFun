class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

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
