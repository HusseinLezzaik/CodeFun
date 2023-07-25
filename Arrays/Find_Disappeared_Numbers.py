# Find All Numbers Disappeared in an Array: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# O(n) time | O(n) space
def findDisappearedNumbers(nums):
    n = len(nums)
    missing_nums = []
    for i in range(n):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    for i in range(n):
        if nums[i] > 0:
            missing_nums.append(i+1)
    return missing_nums

# O(n) time | O(1) space
def find_disappeared_numbers(nums):
    for num in nums:
        index = abs(num) - 1
        nums[index] = - abs(nums[index])
    
    return [i + 1 for i, num in enumerate(nums) if num > 0]
