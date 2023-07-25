# Maximum Subarray: https://leetcode.com/problems/maximum-subarray/

# O(N) time, O(1) space
def maxSubArray(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Test Cases
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Expected output: 6
print(maxSubArray([1]))  # Expected output: 1