# Set Matrix Zeroes: https://leetcode.com/problems/set-matrix-zeroes/

# O(mn) time | O(m + n) space
def setZeroes(matrix):
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

# Test 1: Normal case
matrix1 = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
setZeroes(matrix1)
print(f"Resulting matrix: {matrix1}")
# Expect: [[1,0,1],[0,0,0],[1,0,1]]

# Test 2: Another normal case
matrix2 = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
setZeroes(matrix2)
print(f"Resulting matrix: {matrix2}")
# Expect: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Test 3: Case with all zeroes
matrix3 = [
    [0,0],
    [0,0]
]
setZeroes(matrix3)
print(f"Resulting matrix: {matrix3}")
# Expect: [[0,0],[0,0]]

(matrix1, matrix2, matrix3)