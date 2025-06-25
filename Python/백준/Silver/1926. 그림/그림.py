from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    size = 1

    while queue:
        cy, cx = queue.popleft()
        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and paper[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    size += 1
    return size

count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            count += 1
            max_size = max(max_size, bfs(i, j))

print(count)
print(max_size)
