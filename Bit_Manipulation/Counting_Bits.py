# Counting Bits: https://leetcode.com/problems/counting-bits/

# O(N) time, O(N) space
def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp

# Test Cases
print(countBits(2))  # Expected output: [0, 1, 1]
print(countBits(5))  # Expected output: [0, 1, 1, 2, 1, 2]
print(countBits(8))  # Expected output: [0, 1, 1, 2, 1, 2, 2, 3, 1]