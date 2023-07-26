# Find K Pair with Smallest Sums: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

"""
Time complexity: O(k * log(k)), because we perform k operations and each operation (push or pop) takes log(k) time in a heap of size k.
Space complexity: O(k), because we keep at most k+1 elements in the heap and k elements in the visited set.
"""
import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        visited = set()
        heap = []
        res = []
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited.add((0, 0))
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))
        return res

# Test the kSmallestPairs function
sol = Solution()

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print("The k pairs with the smallest sums are:", sol.kSmallestPairs(nums1, nums2, k))  # Expected: [[1, 2], [1, 4], [1, 6]]
