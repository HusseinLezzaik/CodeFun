# House Robber: https://leetcode.com/problems/house-robber/

# O(N) time, O(1) space
def rob(nums):
    prev1 = prev2 = 0
    for num in nums:
        prev1, prev2 = max(prev2 + num, prev1), prev1
    return prev1

# Test Cases
print(rob([1, 2, 3, 1]))  # Expected output: 4
print(rob([2, 7, 9, 3, 1]))  # Expected output: 12