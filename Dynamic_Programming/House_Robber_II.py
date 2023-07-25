# House Robber II: https://leetcode.com/problems/house-robber-ii/

# O(N) time, O(1) space
def rob(nums):
    def rob_linear(nums):
        prev1 = prev2 = 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
        return prev1

    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Test Cases
print(rob([2, 3, 2]))  # Expected output: 3
print(rob([1, 2, 3, 1]))  # Expected output: 4