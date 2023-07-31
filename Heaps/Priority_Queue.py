# Priority Queue

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def is_empty(self):
        return not self._queue

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        return heapq.heappop(self._queue)[-1]
