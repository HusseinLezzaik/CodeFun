# Seach In Rotated Matrix: https://leetcode.com/problems/search-in-rotated-sorted-array/

"""
The time complexity is O(logn), because we're using a binary search which halves the search space at every step.
The space complexity is O(1), because we're using a constant amount of space to store the indices.
"""

def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # If nums[low..mid] is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # If nums[mid..high] is sorted
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


print(search([4,5,6,7,0,1,2], 0))  # Expected output: 4
print(search([4,5,6,7,0,1,2], 3))  # Expected output: -1
print(search([1], 0))  # Expected output: -1