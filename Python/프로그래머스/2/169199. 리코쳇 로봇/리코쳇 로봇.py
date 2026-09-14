from collections import deque

def solution(board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x_len, y_len = len(board[0]), len(board)

    visited = [[False] * x_len for _ in range(y_len)]


    for y in range(y_len):
        for x in range(x_len):
            if board[y][x] == "R":
                start = (x, y)

    queue = deque()
    queue.append((start[0], start[1], 0))  
    visited[start[1]][start[0]] = True

    while queue:
        cx, cy, count = queue.popleft()

        if board[cy][cx] == "G":
            return count

        for i in range(4):
            nx, ny = cx, cy
            while True:
                tx = nx + dx[i]
                ty = ny + dy[i]
                if 0 <= tx < x_len and 0 <= ty < y_len and board[ty][tx] != "D":
                    nx, ny = tx, ty
                else:
                    break

            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, count + 1))

    return -1  
