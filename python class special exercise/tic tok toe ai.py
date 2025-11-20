import random

# =============================================
# Tic Tac Toe (Rule-Based Computer Player)
# ---------------------------------------------
# - Human plays as "X"
# - Computer plays as "O"
# - The computer uses a logical, rule-based
#   strategy to play intelligently.
# =============================================


def print_board(board):
    """
    Display the current Tic Tac Toe board in a readable format.

    Args:
        board (list[list[str]]): 3x3 list representing the game board.
                                 Each cell contains "X", "O", or " ".
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print() 


def check_winner(board):
    """
    Check the board for a winner.

    Args:
        board (list[list[str]]): The game board.

    Returns:
        str | None: "X" if player X wins, "O" if player O wins, or None if no winner yet.
    """
    # Check rows and columnsss
    for i in range(3):
        # Row check
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        # Column check
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_draw(board):
    """
    Determine whether the game is a draw (no empty spaces left).

    Args:
        board (list[list[str]]): The game board.

    Returns:
        bool: True if all cells are filled and there is no winner.
    """
    return all(cell != " " for row in board for cell in row)


def get_human_move(board):
    """
    Ask the human player to enter a move (row and column).

    Args:
        board (list[list[str]]): The current board.

    Returns:
        tuple[int, int]: The chosen (row, column) coordinates.

    Notes:
        - Valid inputs are integers 0, 1, or 2.
        - Re-prompts until a valid and empty cell is chosen.
    """
    while True:
        try:
            row = int(input("Enter row (0–2): "))
            col = int(input("Enter column (0–2): "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("❌ Please enter numbers between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("⚠️ That cell is already taken. Try again.")
                continue

            return row, col
        except ValueError:
            print("❌ Invalid input. Please enter integers between 0 and 2.")


def get_computer_move(board, computer="O", human="X"):
    """
    Compute the computer's move using a rule-based strategy.

    Strategy priority:
        1. Win if possible.
        2. Block opponent’s immediate win.
        3. Take center if available.
        4. Take a corner if available.
        5. Take a side if available.

    Args:
        board (list[list[str]]): The current board state.
        computer (str): Symbol representing the computer (default "O").
        human (str): Symbol representing the human (default "X").

    Returns:
        tuple[int, int]: Coordinates (row, column) for the computer's move.
    """
    # 1️⃣ Try to win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = computer
                if check_winner(board) == computer:
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "

    # 2️⃣ Block the opponent's winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = human
                if check_winner(board) == human:
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "

    # 3️⃣ Take center
    if board[1][1] == " ":
        return 1, 1

    # 4️⃣ Take one of the corners
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [pos for pos in corners if board[pos[0]][pos[1]] == " "]
    if available_corners:
        return random.choice(available_corners)

    # 5️⃣ Take one of the sides
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    available_sides = [pos for pos in sides if board[pos[0]][pos[1]] == " "]
    if available_sides:
        return random.choice(available_sides)

    # Fallback (should never happen)
    return None


def main():
    """
    Run the Tic Tac Toe game loop (Human vs Rule-Based Computer).
    """
    print("🎮 Welcome to Tic Tac Toe!")
    print("You are 'X' and the computer is 'O'.\n")

    # Initialize empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Human starts first

    # Main game loop
    while True:
        print_board(board)

        # Human move
        if current_player == "X":
            print("Your turn:")
            row, col = get_human_move(board)
        else:
            print("Computer's turn:")
            row, col = get_computer_move(board)
            print(f"💻 Computer chooses: ({row}, {col})")

        # Apply the move
        board[row][col] = current_player

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "X":
                print("🏆 You win! Congratulations!")
            else:
                print("💻 Computer wins! Better luck next time!")
            break

        # Check for draw
        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch turn
        current_player = "O" if current_player == "X" else "X"

    print("\nGame Over. Thanks for playing!")


if __name__ == "__main__":
    main()
