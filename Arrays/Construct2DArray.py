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

