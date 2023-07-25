# Kth Smallest Element in Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# O(Nlog(max element - min element)) time, O(1) space
def count_smaller_or_equal(matrix, mid):
    n = len(matrix)
    count = 0
    row, col = n - 1, 0

    while row >= 0 and col < n:
        if matrix[row][col] <= mid:
            count += row + 1
            col += 1
        else:
            row -= 1

    return count

def kthSmallest(matrix, k):
    n = len(matrix)
    left, right = matrix[0][0], matrix[n - 1][n - 1]

    while left < right:
        mid = left + (right - left) // 2
        count = count_smaller_or_equal(matrix, mid)
        if count < k:
            left = mid + 1
        else:
            right = mid

    return left

# Test Cases
print(kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))  # Expected output: 13
print(kthSmallest([[-5]], 1))  # Expected output: -5