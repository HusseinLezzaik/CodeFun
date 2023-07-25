# Spiral Matrix: https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            result = []
    
            if not matrix:
                return result

            top = 0
            bottom = len(matrix) - 1
            left = 0
            right = len(matrix[0]) - 1

            while top <= bottom and left <= right:
                # Move right
                for j in range(left, right + 1):
                    result.append(matrix[top][j])
                top += 1

                # Move down
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1

                # Move left
                if top <= bottom:
                    for j in range(right, left - 1, -1):
                        result.append(matrix[bottom][j])
                    bottom -= 1

                # Move up
                if left <= right:
                    for i in range(bottom, top - 1, -1):
                        result.append(matrix[i][left])
                    left += 1

            return result
