# Sudoko Solver: https://leetcode.com/problems/sudoku-solver/
"""
The time complexity for this approach can be considered as O(9^(nn)) for a nn board because in a worst-case scenario we may have to check all possibilities.
For a standard 9*9 Sudoku, this will be O(9^81).

The space complexity is O(n*n), for storing the Sudoku board.
"""


def solveSudoku(board):
    def is_valid(board, row, col, num):
        # Check the number in the row
        for x in range(9):
            if board[row][x] == num:
                return False
             
        # Check the number in the column
        for x in range(9):
            if board[x][col] == num:
                return False
 
        # Check the number in the 3*3 matrix
        start_row, start_col = row - row%3, col - col%3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True
 
    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in "123456789":
                        if is_valid(board, i, j, num):
                            board[i][j] = num  # try this number for the current cell
 
                            if solve(board):  # recurse on the result
                                return True
                            
                            board[i][j] = '.'  # undo the current cell for backtracking
                    return False  # trigger backtracking
        return True  # sudoku solved
 
    if board is None or len(board) == 0:
        return None
    solve(board)
    return board

# Test Cases
def print_board(board):
    for row in board:
        print(row)

test_1 = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

print_board(solveSudoku(test_1))
