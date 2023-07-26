# Sliding Window Median: https://leetcode.com/problems/sliding-window-median/

'''
The time complexity of the medianSlidingWindow function is  O(nlogk), where n is the length of the input array and k is the size of the sliding window.
This is because for each of the n elements in the array, we perform operations (adding and removing elements) that take O(logk) time in a sorted list of size k.

The space complexity is O(k) because we store the elements of the sliding window in a sorted list, which takes O(k) space.
'''

from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums, k):
        window = SortedList(nums[:k])
        medians = []
        for i in range(k, len(nums) + 1):
            medians.append((window[(k - 1) // 2] + window[k // 2]) / 2.0)
            if i < len(nums):
                window.remove(nums[i - k])
                window.add(nums[i])
        return medians

# Test the medianSlidingWindow function
sol = Solution()

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print("The medians are:", sol.medianSlidingWindow(nums, k))  # return [1.0,-1.0,-1.0,3.0,5.0,6.0]
