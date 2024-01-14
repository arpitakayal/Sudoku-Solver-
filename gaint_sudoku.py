def is_valid(board, row, col, num):
    # Check if the number already exists in the row
    for i in range(len(board)):
        if board[row][i] == num:
            return False

    # Check if the number already exists in the column
    for i in range(len(board)):
        if board[i][col] == num:
            return False

    # Check if the number already exists in the sub-grid
    subgrid_size = int(len(board) ** 0.5)
    start_row = (row // subgrid_size) * subgrid_size
    start_col = (col // subgrid_size) * subgrid_size
    for i in range(subgrid_size):
        for j in range(subgrid_size):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                for num in range(1, len(board) + 1):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# Example giant Sudoku puzzle to solve (0 represents an empty cell)
board = [
    [0, 3, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 15, 4],
    [10, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 14, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 2, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [12, 0, 0, 0, 0, 15, 0, 0, 2, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 11, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3],
    [13, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]
]


if solve_sudoku(board):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists.")