def solution(m, n, board):
    board = [list(row) for row in board]
    total_removed = 0

    while True:
        remove_set = set()

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != ' ':
                    block = board[i][j]
                    if (board[i][j+1] == block and
                        board[i+1][j] == block and
                        board[i+1][j+1] == block):
                        remove_set.update({(i, j), (i, j+1), (i+1, j), (i+1, j+1)})

        if not remove_set:
            break

        for x, y in remove_set:
            board[x][y] = ' '
        total_removed += len(remove_set)

        for j in range(n):
            empty_row = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] != ' ':
                    board[empty_row][j] = board[i][j]
                    if empty_row != i:
                        board[i][j] = ' '
                    empty_row -= 1

    return total_removed

