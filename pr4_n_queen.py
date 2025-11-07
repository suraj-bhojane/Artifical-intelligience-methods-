def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "-" for cell in row))

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = False
    return False

if __name__ == "__main__":
    n = int(input("Enter N: "))
    board = [[False for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0, n):
        print("Solution:")
        print_board(board)
    else:
        print("No solution exists")
