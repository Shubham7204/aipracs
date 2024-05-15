import math

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -10
    elif check_winner(board, 'O'):
        return 10
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = '-'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = '-'
                    best_score = min(score, best_score)
        return best_score

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != '-' for row in board for cell in row)

def best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = '-'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Define the initial state of the board
board = [
    ['X', '-', 'O'],
    ['-', 'X', 'O'],
    ['-', '-', '-']
]

print("Current Board:")
for row in board:
    print(" ".join(row))

print("\nBest Move for 'O' (row, column):", best_move(board))