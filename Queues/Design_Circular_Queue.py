# Design Circular Queue: https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * (k + 1)
        self.headIndex = 0
        self.count = 0
        self.capacity = k + 1

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity - 1:
            return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity - 1
        

# Now let's test our circular queue
cq = MyCircularQueue(3)
print(cq.enQueue(1))  # returns True
print(cq.enQueue(2))  # returns True
print(cq.enQueue(3))  # returns True
print(cq.enQueue(4))  # returns False, queue is full
print(cq.Rear())  # returns 3, last item in the queue
print(cq.isFull())  # returns True, queue is full
print(cq.deQueue())  # returns True, dequeue operation successful
print(cq.enQueue(4))  # returns True, enqueue operation successful
print(cq.Rear())  # returns 4, last item in the queue
