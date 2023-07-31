## Implement Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/

# O(1) time for push, O(1) amortized time for pop, O(1) time for peek, O(1) time for empty
# O(n) space
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Now let's test our queue
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # returns 1
print(q.pop())   # returns 1
print(q.empty()) # returns False
