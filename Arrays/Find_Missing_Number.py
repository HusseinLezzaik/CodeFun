# Find the missing number in the array: https://leetcode.com/problems/missing-number/

def missingNumber(nums):
    n = len(nums)
    expected_sum = (n * (n+1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

