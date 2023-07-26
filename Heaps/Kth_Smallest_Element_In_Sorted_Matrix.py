# Kth Smallest Element in Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

"""
Time complexity: O(n * log(max - min)), where n is the length of the matrix's side, max is the maximum element in the matrix, and min is the minimum element. The binary search costs log(max - min), and for each mid value, we need to count the elements not larger than mid, which costs O(n).
Space complexity: O(1), as we only use a few integer variables.
"""

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        def countLessEqual(mid):
            i, j = n - 1, 0
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    cnt += i + 1
                    j += 1
                else:
                    i -= 1
            return cnt

        low, high = matrix[0][0], matrix[n-1][n-1]
        while low < high:
            mid = low + (high - low) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

# Test the kthSmallest function
sol = Solution()

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print("The kth smallest element in the matrix is:", sol.kthSmallest(matrix, k))  # Expected: 13