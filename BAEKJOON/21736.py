import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())

def bfs(s, uni, N, M):
    friends = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited = [[False] * M for _ in range(N)]  # 방문 여부 확인
    queue = deque()
    queue.append(s)
    
    while queue:
        x, y = queue.popleft()  
        if visited[y][x]:  
            continue
        visited[y][x] = True
        if uni[y][x]=="P":
            friends+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:  
                if uni[ny][nx] == "O":
                    queue.append((nx, ny))
                elif uni[ny][nx] == "P":
                    queue.append((nx,ny))
  

    return friends if friends else "TT"

university = []
start = None
for j in range(N):
    row = list(input().strip())  
    university.append(row)
    for i in range(M):
        if row[i] == "I":  
            start = (i, j)

print(bfs(start, university, N, M))
