#  209. Minimum Size Subarray Sum: https://leetcode.com/problems/minimum-size-subarray-sum/description/

# O(N) time, O(1) space
def minSubArrayLen(target, nums):
    start = 0
    min_length = float('inf')
    window_sum = 0

    for end in range(len(nums)):
        window_sum += nums[end]
        while window_sum >= target:
            min_length = min(min_length, end - start + 1)
            window_sum -= nums[start]
            start += 1

    return 0 if min_length == float('inf') else min_length

# Test cases
print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Expected output: 2
print(minSubArrayLen(4, [1, 4, 4]))  # Expected output: 1
