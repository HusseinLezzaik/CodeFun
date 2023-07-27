# Knapsack Problem (Also known as Target Sum): https://leetcode.com/problems/target-sum/description/

"""
The time complexity is O(nW), where n is the number of elements in nums and W is the sum of the elements. This is because we're filling a 1D DP array of size W+1 for each element in nums.

The space complexity is O(W), because we're using a 1D DP array of size W+1.
"""

def findTargetSumWays(nums, target):
    total = sum(nums)
    if total < target or (total + target) % 2:
        return 0

    W = (total + target) // 2
    dp = [0] * (W + 1)
    dp[0] = 1
    for num in nums:
        for i in range(W, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[W]

print(findTargetSumWays([1,1,1,1,1], 3))  # Expected output: 5
print(findTargetSumWays([1], 1))  # Expected output: 1