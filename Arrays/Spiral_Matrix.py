# Spiral Matrix: https://leetcode.com/problems/spiral-matrix/

# First, let's remove the class method format and convert the function to a normal Python function
# Also, the type hint List[List[int]] and List[int] are not necessary here

# O(mn) time | O(mn) space
def spiralOrder(matrix):
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

# Test 1: Normal case
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
spiral1 = spiralOrder(matrix1)
print(f"For the input matrix, the spiral order is {spiral1}. Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]")

# Test 2: Another normal case
matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
spiral2 = spiralOrder(matrix2)
print(f"For the input matrix, the spiral order is {spiral2}. Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]")

# Test 3: Case with single row
matrix3 = [
    [1, 2, 3, 4, 5]
]
spiral3 = spiralOrder(matrix3)
print(f"For the input matrix, the spiral order is {spiral3}. Expected: [1, 2, 3, 4, 5]")

(spiral1, spiral2, spiral3)