import numpy as np

# Function to print the board
def board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if a player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax function to determine the best move
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):  # AI win
        return 10 - depth
    if check_winner(board, "X"):  # Human win
        return depth - 10
    if is_full(board):  # Draw
        return 0

    if is_maximizing:
        max_eval = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move
def best_move(board):
    best_val = -np.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the AI is 'O'.")
    board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as 0, 1, or 2.")

        board(board)
        if check_winner(board, "X"):
            print("Congratulations! You won!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI's turn...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        board(board)
        if check_winner(board, "O"):
            print("The AI wins! Better luck next time!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()

