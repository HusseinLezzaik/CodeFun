# Longest Increasing Subsequence: https://leetcode.com/problems/longest-increasing-subsequence/

# O(N^2) time, O(N) space
def lengthOfLIS(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Test Cases
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected output: 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))  # Expected output: 4
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # Expected output: 1