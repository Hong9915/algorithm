import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

mirro = []

for i in range(N):
    line = input().strip()
    row = [int(char) for char in line]
    mirro.append(row)

def bfs(y, x, n, m, mirro):
    dx = [0, 0, -1, 1]  # 좌우 이동
    dy = [-1, 1, 0, 0]  # 상하 이동

    dist = [[-1 for _ in range(m)] for _ in range(n)]
    dq = deque([(y, x)])
    dist[y][x] = 1  # 시작 위치의 거리를 1로 설정

    while dq:
        y, x = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n and mirro[ny][nx] == 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                dq.append((ny, nx))

    return dist[n - 1][m - 1]  # 출구까지의 거리 반환

# BFS 실행
result = bfs(0, 0, N, M, mirro)
print(result)
