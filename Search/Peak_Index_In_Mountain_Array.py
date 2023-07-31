# Peak Index In Mountain Array: https://leetcode.com/problems/peak-index-in-a-mountain-array/

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
print(findPeakElement([0, 1, 0]))  # Expected output: 1
print(findPeakElement([0, 2, 1, 0]))  # Expected output: 1
print(findPeakElement([0, 10, 5, 2]))  # Expected output: 1