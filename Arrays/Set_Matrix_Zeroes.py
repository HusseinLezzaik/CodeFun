# Set Matrix Zeroes: https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_length = len(matrix)
        columns_length = len(matrix[0])
        
        rows, cols = set(), set()
        
        for i in range(rows_length):
            for j in range(columns_length):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(rows_length):
            for j in range(columns_length):
                if i in rows or j in cols:
                    matrix[i][j] = 0
