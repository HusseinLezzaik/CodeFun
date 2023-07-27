# First Missing Positive: https://leetcode.com/problems/first-missing-positive/description/

# O(n) time | O(1) space
def firstMissingPositive(nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Iterate through the sorted array to find the first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all positive integers are in the array, return the next integer (n+1)
        return n + 1

# Test 1: Normal case
nums1 = [3, 4, -1, 1]
missing1 = firstMissingPositive(nums1)
print(f"For the input {nums1}, the first missing positive number is {missing1}. Expected: 2")

# Test 2: Another normal case
nums2 = [1, 2, 0]
missing2 = firstMissingPositive(nums2)
print(f"For the input {nums2}, the first missing positive number is {missing2}. Expected: 3")

# Test 3: Case with smallest possible list
nums3 = [7, 8, 9, 11, 12]
missing3 = firstMissingPositive(nums3)
print(f"For the input {nums3}, the first missing positive number is {missing3}. Expected: 1")

(missing1, missing2, missing3)