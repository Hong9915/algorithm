import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# BFS 초기 설정
def bfs():
    queue = deque([(0, 0, 0)])  
    visited[0][0][0] = 1  

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, chance = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][chance]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][chance] == 0:
                visited[nx][ny][chance] = visited[x][y][chance] + 1
                queue.append((nx, ny, chance))

            elif graph[nx][ny] == 1 and chance == 0 and visited[nx][ny][1] == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))

    return -1  # 도달 불가능

print(bfs())
