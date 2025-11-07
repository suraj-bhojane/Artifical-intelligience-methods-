def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)  # horizontal line between rows


def is_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def evaluate(board):
    if is_winner(board, 'X'):
        return 10
    elif is_winner(board, 'O'):
        return -10
    return 0


def alpha_beta(board, depth, is_max, alpha, beta):
    score = evaluate(board)
    if score != 0 or is_full(board):
        return score

    if is_max:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = alpha_beta(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        return max_eval  # prune remaining branches
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = alpha_beta(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        return min_eval  # prune remaining branches
        return min_eval


def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = alpha_beta(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move


if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Enter the current board state (use X, O, space):")
    for i in range(3):
        row_str = input(f"Row {i}: ")
        row = list(row_str.ljust(3, ' '))
        board[i] = row

    print("\nCurrent board:")
    print_board(board)

    if not is_full(board) and not is_winner(board, 'X') and not is_winner(board, 'O'):
        move = find_best_move(board)
        print(f"\nBest move for X: {move}")
        board[move[0]][move[1]] = 'X'
        print("\nBoard after move:")
        print_board(board)
    else:
        print("\nGame over")
