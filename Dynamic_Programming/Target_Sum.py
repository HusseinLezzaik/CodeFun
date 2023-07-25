# Target Sum: https://leetcode.com/problems/target-sum/

# O(N*sum) time, O(N*sum) space
def findTargetSumWays(nums, target):
    sum_nums = sum(nums)
    if abs(target) > sum_nums:
        return 0

    offset = sum_nums
    dp = [[0] * (2*sum_nums+1) for _ in range(len(nums)+1)]
    dp[0][offset] = 1

    for i in range(1, len(nums)+1):
        for j in range(2*sum_nums+1):
            if j+nums[i-1] < 2*sum_nums+1:
                dp[i][j] += dp[i-1][j+nums[i-1]]
            if j-nums[i-1] >= 0:
                dp[i][j] += dp[i-1][j-nums[i-1]]

    return dp[len(nums)][target+offset]

# Test Cases
print(findTargetSumWays([1, 1, 1, 1, 1], 3))  # Expected output: 5
print(findTargetSumWays([1], 1))  # Expected output: 1
print(findTargetSumWays([1, 0], 1))  # Expected output: 2