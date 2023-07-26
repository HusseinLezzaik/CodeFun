# 632. Smallest Range Covering Elements from K Lists: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

"""
Time complexity: O(N log k), where N is the total number of elements in all lists and k is the number of lists. This is because we process each element in the lists once and a heap operation takes log k time.
Space complexity: O(k), because we keep at most k pointers to elements in the heap.
"""

import heapq

class Solution:
    def smallestRange(self, nums):
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in nums)

        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))

# Test the smallestRange function
sol = Solution()

nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print("The smallest range is:", sol.smallestRange(nums))  # Expected: [20, 24]


