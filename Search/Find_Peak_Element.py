# Find Peak Element: https://leetcode.com/problems/find-peak-element/

# O(logN) time, O(1) space
def findPeakElement(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

# Test Cases
print(findPeakElement([1, 2, 3, 1]))  # Expected output: 2
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Expected output: 1 or 5
print(findPeakElement([1, 2]))  # Expected output: 1