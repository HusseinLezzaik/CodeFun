"""
LeetCode: https://leetcode.com/problems/kth-largest-element-in-a-stream/

the main idea of using heaps, is order matters a lot to solve the problem; ideally every step looking for min/max
sorting is more expensive than heaps, so heaps for the rescue with log insert/delete 

the questions are very fun and easy to do, and heaps are very straight forward to use

some notes:
- on time complexity: many times it's O(n + klogn) since O(n) to build heap, and O(klogn) to pop k times
- you can heapify something like [[1, 2], [3, 4], [5, 6]] and it will heapify based on the first element and pop them togehter [a, b]
- with kth kind of question, sometimes its sufficient to only track/build a heap of size k
"""

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
