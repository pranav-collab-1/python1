def evaluate(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            if board[a] == "X":
                return 10
            elif board[a] == "O":
                return -10

    return 0


def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def find_best_move(board):
    best_val = -1000
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            move_val = minimax(board, 0, False)
            board[i] = " "

            if move_val > best_val:
                best_val = move_val
                best_move = i

    return best_move


board = [" "] * 9


def print_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")


while " " in board and evaluate(board) == 0:
    print_board()

    opponent_move = int(input("Enter position (0-8): "))

    if board[opponent_move] != " ":
        print("Invalid move!")
        continue

    board[opponent_move] = "O"

    if evaluate(board) != 0 or " " not in board:
        break

    player1_move = find_best_move(board)
    board[player1_move] = "X"

    print(f"\nPlayer 1 chose position {player1_move}\n")


print_board()

final_score = evaluate(board)

if final_score > 0:
    print("Player 1 Wins!")
elif final_score < 0:
    print("Opponent Won!")
else:
    print("It's a Draw!")
