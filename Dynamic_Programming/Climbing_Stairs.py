# Climbing Stairs: https://leetcode.com/problems/climbing-stairs/

# O(N) time, O(N) space
def climbStairs(n):
    if n <= 2:
        return n
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

# Test Cases
print(climbStairs(2))  # Expected output: 2
print(climbStairs(3))  # Expected output: 3