# Write python function to test if someone won in the board game Connect4


# O(n^2) time | O(1) space
def check_winner(board):

    # Check for horizontal wins
    for row in board:
        for i in range(len(row) - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] and row[i] != '.':
                return row[i]
    
    # Check for vertical wins
    for j in range(len(board[0])):
        for i in range(len(board) - 3):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] and board[i][j] != '.':
                return board[i][j]
    
    # Check for diagonal wins
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] and board[i][j] != '.':
                return board[i][j]
            if board[i][j+3] == board[i+1][j+2] == board[i+2][j+1] == board[i+3][j] and board[i][j+3] != '.':
                return board[i][j+3]
    return None

# Example usage
board = [['.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'X', '.', '.', '.'],
         ['.', '.', 'X', 'O', '.', '.', '.'],
         ['.', 'X', 'O', 'X', 'O', '.', '.'],
         ['X', 'O', 'X', 'O', 'X', 'O', '.']]
print(check_winner(board)) # Output: 'X'
