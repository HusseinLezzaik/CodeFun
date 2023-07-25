# Maximum Average Subarray I: https://leetcode.com/problems/maximum-average-subarray-i/solutions/

# O(N) time, O(1) space
def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum / k

# Test cases
print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # Expected output: 12.75
print(findMaxAverage([5], 1))  # Expected output: 5