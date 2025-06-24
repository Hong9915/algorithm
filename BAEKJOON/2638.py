import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    melt = []  

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if paper[nx][ny] == 1:
                    continue  
                queue.append((nx, ny))  

    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1:  
                air_count = 0 
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < N and 0 <= nj < M and paper[ni][nj] == 0 and visited[ni][nj]:
                        air_count += 1
                if air_count >= 2: 
                    melt.append((i, j))


    for x, y in melt:
        paper[x][y] = 0

    return len(melt)

time = 0
while True:
    melt_count = bfs()
    if melt_count == 0:
        break  
    time += 1

print(time)
