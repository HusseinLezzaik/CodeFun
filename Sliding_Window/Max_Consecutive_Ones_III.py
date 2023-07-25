# Max Consecutive Ones III: https://leetcode.com/problems/max-consecutive-ones-iii/

# O(N) time, O(1) space
def longestOnes(nums, k):
    start = 0
    zero_count = 0
    max_length = 0

    for end in range(len(nums)):
        if nums[end] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[start] == 0:
                zero_count -= 1
            start += 1
        max_length = max(max_length, end - start + 1)

    return max_length

# Test Cases
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 3)) # 10
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 4)) # 11