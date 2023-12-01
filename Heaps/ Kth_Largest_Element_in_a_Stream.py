"""
LeetCode: https://leetcode.com/problems/kth-largest-element-in-a-stream/

the main idea of using heaps, is order matters a lot to solve the problem; ideally every step looking for min/max
sorting is more expensive than heaps, so heaps for the rescue with log insert/delete 

the questions are very fun and easy to do, and heaps are very straight forward to use
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
