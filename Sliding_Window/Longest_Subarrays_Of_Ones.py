# Longest Subarray of 1's After Deleting One Element: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

# O(N) time, O(1) space
def longestSubarray(nums):
    start = 0
    zero_count = 0
    max_length = 0

    for end in range(len(nums)):
        if nums[end] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[start] == 0:
                zero_count -= 1
            start += 1
        max_length = max(max_length, end - start)

    return max_length

# Test Cases
print(longestSubarray([1,1,0,1]))  # Expected output: 3
print(longestSubarray([0,1,1,1,0,1,1,0,1]))  # Expected output: 5