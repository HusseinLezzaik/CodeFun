# Minimum Number of K Consecutive Bit Flips: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

from collections import deque

# O(N) time, O(N) space
def minKBitFlips(nums, k):
    queue = deque()
    flip = 0

    for i in range(len(nums)):
        if queue and i >= queue[0] + k:
            flip -= queue.popleft()

        if flip % 2 == nums[i]:
            if i + k > len(nums):
                return -1
            queue.append(i)
            flip += 1

    return flip

# Test Cases
print(minKBitFlips([0,1,0], 1)) # 2
print(minKBitFlips([1,1,0], 2)) # -1