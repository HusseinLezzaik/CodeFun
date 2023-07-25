# 239. Sliding Window Maximum: https://leetcode.com/problems/sliding-window-maximum/

from collections import deque

# O(N) time, O(k) space
def maxSlidingWindow(nums, k):
    deque = collections.deque()
    max_values = []

    for i in range(len(nums)):
        while deque and nums[i] > nums[deque[-1]]:
            deque.pop()
        deque.append(i)
        if deque[0] < i - k + 1:
            deque.popleft()
        if i >= k - 1:
            max_values.append(nums[deque[0]])

    return max_values

# Test Cases
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
print(maxSlidingWindow([1], 1)) # [1]