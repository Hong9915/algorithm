import sys
from collections import deque

input = sys.stdin.readline
def bfs(picture, visited, start, color):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(picture) and 0 <= ny < len(picture) and not visited[nx][ny]:
                if picture[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    
def colorblind_bfs(picture, visited_colorblind, start, color):
    queue = deque([start])
    visited_colorblind[start[0]][start[1]] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(picture) and 0 <= ny < len(picture) and not visited_colorblind[nx][ny]:
                if color=='R':
                    if picture[nx][ny] == "R" or picture[nx][ny] == "G":
                        visited_colorblind[nx][ny] = True
                        queue.append((nx, ny))
                else :
                    if picture[nx][ny] == color:
                        visited_colorblind[nx][ny] = True
                        queue.append((nx, ny))

N = int(input().strip())
picture = []

for i in range(N):
    row = input().strip()
    picture.append(list(row))


visited = [[False] * N for _ in range(N)]
visited_colorblind = [[False] * N for _ in range(N)]

normal_count = 0
colorblind_count = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(picture, visited, (i, j), picture[i][j])
            normal_count += 1

for i in range(N):
    for j in range(N):
        if not visited_colorblind[i][j]:
            if picture[i][j] == 'R' or picture[i][j] == 'G':
                colorblind_bfs(picture, visited_colorblind, (i, j), 'R')
            else:
                colorblind_bfs(picture, visited_colorblind, (i, j), picture[i][j])
            colorblind_count += 1

# 결과 출력
print(normal_count, colorblind_count)


