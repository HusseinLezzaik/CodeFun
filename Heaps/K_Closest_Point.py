# K Closest Points to Origin: https://leetcode.com/problems/k-closest-points-to-origin/

"""
Time complexity: O(n log k), where n is the total number of points. We are offering each point to the heap, which takes log k time (where k is the size of the heap).
Space complexity: O(k), because we store k points in the heap.
"""

import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x,y) for (dist,x, y) in heap]

# Test the kClosest function
sol = Solution()

points = [[1,3],[-2,2]]
k = 1
print("The k closest points to the origin are:", sol.kClosest(points, k))  # Expected: [[-2, 2]]
