# Single Number: https://leetcode.com/problems/single-number/

# O(n) time | O(n) space
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test 1: Normal case
nums1 = [4,1,2,1,2]
single1 = singleNumber(nums1)
print(f"For the input {nums1}, the single number is {single1}. Expected: 4")

# Test 2: Another normal case
nums2 = [2,2,1]
single2 = singleNumber(nums2)
print(f"For the input {nums2}, the single number is {single2}. Expected: 1")

# Test 3: Case with single element in the list
nums3 = [1]
single3 = singleNumber(nums3)
print(f"For the input {nums3}, the single number is {single3}. Expected: 1")

(single1, single2, single3)
