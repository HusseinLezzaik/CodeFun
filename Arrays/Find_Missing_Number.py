# Find the missing number in the array: https://leetcode.com/problems/missing-number/

# O(n) time | O(1) space
def missingNumber(nums):
    n = len(nums)
    expected_sum = (n * (n+1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Test 1: Normal case
nums1 = [3, 0, 1]
missing1 = missingNumber(nums1)
print(f"For the input {nums1}, the missing number is {missing1}. Expected: 2")

# Test 2: Another normal case
nums2 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
missing2 = missingNumber(nums2)
print(f"For the input {nums2}, the missing number is {missing2}. Expected: 8")

# Test 3: When the missing number is 0
nums3 = [1]
missing3 = missingNumber(nums3)
print(f"For the input {nums3}, the missing number is {missing3}. Expected: 0")

(missing1, missing2, missing3)