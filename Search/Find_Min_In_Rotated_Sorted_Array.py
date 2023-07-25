# Find Minimum in Rotated Sorted Array: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# O(logN) time, O(1) space
def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[right]

# Test Cases
print(findMin([3, 4, 5, 1, 2]))  # Expected output: 1
print(findMin([4, 5, 6, 7, 0, 1, 2]))  # Expected output: 0