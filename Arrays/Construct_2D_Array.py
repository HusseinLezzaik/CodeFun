# O(m*n) time, O(m*n) space
def construct2DArray(original, m, n):
    if len(original) != m * n:
        return []

    result = [[0] * n for _ in range(m)]
    row, col = 0, 0
    for num in original:
        result[row][col] = num
        col += 1
        if col == n:
            col = 0
            row += 1
    
    return result

# Test 1: Normal case
test1 = construct2DArray([1, 2, 3, 4, 5, 6], 2, 3)
print(test1) # Expect: [[1, 2, 3], [4, 5, 6]]

# Test 2: Another normal case with different dimensions
test2 = construct2DArray([1, 2, 3, 4, 5, 6], 3, 2)
print(test2) # Expect: [[1, 2], [3, 4], [5, 6]]

# Test 3: If original is empty, result should also be empty
test3 = construct2DArray([], 0, 0)
print(test3) # Expect: []

# Test 4: If dimensions don't match size of original, return empty list
test4 = construct2DArray([1, 2, 3, 4, 5, 6], 2, 2) 
print(test4) # Expect: []