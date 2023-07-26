# Find Median From Data Stream: https://leetcode.com/problems/find-median-from-data-stream/

"""
The time complexity of both the addNum and findMedian functions is O(logn), where n is the number of elements in the data stream.
This is because we use a heap data structure, and both insertion and deletion in a heap take O(logn) time.

The space complexity is O(n) because we store the elements of the data stream in two heaps, which together can take up to n space.
"""

from heapq import *

class MedianFinder:
    def __init__(self):
        # Initialize two heaps: max_heap for the first half of the data, min_heap for the second half
        self.max_heap = []  # contains the smaller half of the numbers
        self.min_heap = []  # contains the larger half of the numbers

    def addNum(self, num):
        # If the max heap is empty, or the number is smaller than the largest number in the max heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        # Balance the heaps so that the length of max_heap is either equal to or one more than the length of min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:  # max_heap must have one extra element
            return -self.max_heap[0] / 1.0

# Test the MedianFinder class
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())  # return 1.5
mf.addNum(3)
print(mf.findMedian())  # return 2