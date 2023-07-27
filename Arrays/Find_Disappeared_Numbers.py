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

# Test 1: Normal case
test1 = find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1])
print(test1) # Expect: [5, 6] because 5 and 6 are not present in the list

# Test 2: No numbers are missing
test2 = find_disappeared_numbers([1, 2, 3, 4])
print(test2) # Expect: [] because all numbers from 1 to 4 are present

# Test 3: All numbers are missing
test3 = find_disappeared_numbers([2, 2, 2, 2])
print(test3) # Expect: [1, 3, 4] because 1, 3, 4 are not present in the list