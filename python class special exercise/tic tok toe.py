import random

# ===============================
# Enhanced Tic Tac Toe (Console)
# Supports Human vs Computer
# ===============================


def print_board(board):
    """Display the Tic Tac Toe board in a readable format."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()


def check_winner(board):
    """Return the winner ('X' or 'O') if there is one, else None."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_draw(board):
    """Return True if the board is full and there is no winner."""
    return all(cell != " " for row in board for cell in row)


def get_computer_move(board):
    """Pick a random empty cell for the computer."""
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells) if empty_cells else None


def get_human_move(board, current_player):
    """Prompt the human player for a move, with full validation."""
    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0–2): "))
            col = int(input(f"Player {current_player}, enter column (0–2): "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("❌ Invalid input. Please enter numbers between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("⚠️ That cell is already taken. Try again.")
                continue
            return row, col
        except ValueError:
            print("❌ Invalid input. Please enter integers between 0 and 2.")


def main():
    print("🎮 Welcome to Tic Tac Toe!")
    print("Choose game mode:")
    print("1. Human vs Human")
    print("2. Human vs Computer")

    mode = input("Enter your choice (1 or 2): ").strip()
    while mode not in {"1", "2"}:
        mode = input("Invalid choice. Enter 1 or 2: ").strip()

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if mode == "2" and current_player == "O":
            # Computer move
            row, col = get_computer_move(board)
            print(f"💻 Computer chooses: ({row}, {col})")
        else:
            # Human move
            row, col = get_human_move(board, current_player)

        board[row][col] = current_player

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🏆 Player {winner} wins!")
            break

        # Check for draw
        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    print("Game over. Thanks for playing!")


if __name__ == "__main__":
    main()


# A simple command-line Tic Tac Toe game for two players.
# Players take turns to enter their moves.
# The game checks for a win or a draw after each move.
# The board is displayed after each move.
# The game ends when there is a winner or the board is full (draw).
# Players are prompted to enter row and column indices (0, 1, or 2) for their moves.
# Players are represented by "X" and "O".
# The game handles invalid moves by prompting the player to try again.
# The game uses a 3x3 list to represent the board.
# The game checks for wins in rows, columns, and diagonals.
# The game uses functions to organize code for printing the board, checking for a winner, and checking for a draw.
# The game uses a while loop to continue until there is a winner or a draw.
# The game starts with player "X".
# The game alternates turns between players "X" and "O".
# The game is run by calling the main function when the script is executed directly.
# The game is written in Python 3 and can be run in any environment that supports Python 3.
