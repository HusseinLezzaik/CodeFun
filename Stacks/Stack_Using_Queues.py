# Implement Stack Using Queues: https://leetcode.com/problems/implement-stack-using-queues/
"""
the main trick with stacks is that usually we're conducting certain operations, and we need a temporary array 
that we can refer to, and many times we end up using a stack for that.

questions are pretty easy and fun, whenever you're thinking how do i setup this problem and keep track of things, think of how to use a stack to make your life easier!
"""



from collections import deque

"""
# Time complexity:
- push: O(n) because we dump all n elements from queue2 to queue1.
- pop: O(1) because we just pop from the front of queue2.
- peek: O(1) because we just return the first element of queue2.
- is_empty: O(1) because we just check if queue2 is empty.

# Space Complexity: O(n) because we use two queues to store n elements.
"""

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue2.popleft()

    def peek(self) -> int:
        return self.queue2[0]

    def is_empty(self) -> bool:
        return not self.queue2

# Initialize an object of MyStack class
mystack = MyStack()

# Push elements onto the stack
mystack.push(1)
mystack.push(2)
mystack.push(3)

# Retrieve the peek element
print(mystack.peek())  # Outputs: 3

# Check if the stack is empty
print(mystack.is_empty())  # Outputs: False

# Pop an element from the stack
print(mystack.pop())  # Outputs: 3

# Check the peek element again
print(mystack.peek())  # Outputs: 2
