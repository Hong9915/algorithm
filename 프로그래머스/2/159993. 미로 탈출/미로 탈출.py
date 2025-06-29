from collections import deque

def bfs(start, end, maps):
    len_y, len_x = len(maps), len(maps[0])
    visited = [[False]*len_x for _ in range(len_y)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        y, x, time = queue.popleft()
        if (y, x) == end:
            return time
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < len_y and 0 <= nx < len_x:
                if not visited[ny][nx] and maps[ny][nx] != 'X':
                    visited[ny][nx] = True
                    queue.append((ny, nx, time + 1))
    return -1

def solution(maps):
    len_y, len_x = len(maps), len(maps[0])
    for i in range(len_y):
        for j in range(len_x):
            if maps[i][j] == 'S':
                start = (i, j)
            if maps[i][j] == 'E':
                end = (i, j)
            if maps[i][j] == 'L': 
                lever = (i, j)

    to_lever = bfs(start, lever, maps)
    if to_lever == -1:
        return -1


    to_exit = bfs(lever, end, maps)
    if to_exit == -1:
        return -1

    return to_lever + to_exit
