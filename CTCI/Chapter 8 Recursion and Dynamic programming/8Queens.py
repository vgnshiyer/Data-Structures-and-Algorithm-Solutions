posDiagonals = set()
negDiagonals =set()

def place(board, i, j) -> list:
    board[i][j] = 'Q'
    posDiagonals.add(i + j)
    negDiagonals.add(i - j)
    return board

def remove(board, i, j) -> list:
    board[i][j] = '*'
    posDiagonals.remove(i + j)
    negDiagonals.remove(i - j)
    return board

def safeRow(board, r) -> bool:
    for i in range(8):
        if board[r][i] == 'Q':
            return False
    return True

def safeCol(board, c) -> bool:
    for i in range(8):
        if board[i][c] == 'Q':
            return False
    return True

def safeDiagonal(i, j) -> bool:
    return (i + j) not in posDiagonals and (i - j) not in negDiagonals

def placeQueens(board: list, row: int) -> None:
    if row == 8:
        printBoard(board)
        return

    for i in range(8):
        if safeCol(board, i) and safeDiagonal(row, i):
            board = place(board, row, i)
            placeQueens(board, row + 1)
            board = remove(board, row, i)


def printBoard(board: list) -> None:
    n = len(board)

    print('-' * 50)
    for row in board:
        print(row)

if __name__ == '__main__':
    board = [['*'] * 8 for i in range(8)]

    placeQueens(board, 0)