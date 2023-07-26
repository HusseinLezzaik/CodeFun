# Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/
"""
Time complexity: O(n log k), where n is the number of points, because we process each point in the input list once and a heap operation takes log k time.
Space complexity: O(k), because we keep at most k points in the heap
"""


import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []
        for point in points:
            distance = -(point[0]**2 + point[1]**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (distance, point))
            else:
                heapq.heappush(heap, (distance, point))
        return [point for (distance, point) in heap]

# Test the kClosest function
sol = Solution()

points = [[1,3],[-2,2]]
k = 1
print("The k closest points to the origin are:", sol.kClosest(points, k))  # Expected: [[-2, 2]]
