# Find K Closest Elements: https://leetcode.com/problems/find-k-closest-elements/

# O(N) time, O(1) space
def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - 1

    while right - left >= k:
        if x - arr[left] <= arr[right] - x:
            right -= 1
        else:
            left += 1

    return arr[left:left + k]

# Test Cases
print(findClosestElements([1, 2, 3, 4, 5], 4, 3))  # Expected output: [1, 2, 3, 4]
print(findClosestElements([1, 2, 3, 4, 5], 4, -1))  # Expected output: [1, 2, 3, 4]
print(findClosestElements([1, 2, 3, 4, 5], 4, 6))  # Expected output: [2, 3, 4, 5]