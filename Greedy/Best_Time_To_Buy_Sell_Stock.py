# Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# O(N) time, O(1) space
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Test Cases
print(maxProfit([7,1,5,3,6,4]))  # Expected output: 5
print(maxProfit([7,6,4,3,1]))  # Expected output: 0
print(maxProfit([2,4,1]))  # Expected output: 2