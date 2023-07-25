# Coin Change: https://leetcode.com/problems/coin-change/

# O(N * amount) time, O(amount) space
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# test cases
print(coinChange([1, 2, 5], 11))  # Expected output: 3
print(coinChange([2], 3))  # Expected output: -1