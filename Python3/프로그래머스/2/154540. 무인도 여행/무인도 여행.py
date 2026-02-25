from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    answer = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and not visited[i][j]:
                
                queue = deque([(i, j)])
                visited[i][j] = True
                total = int(maps[i][j])
                
                while queue:
                    x, y = queue.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if 0 <= nx < n and 0 <= ny < m:
                            if maps[nx][ny] != "X" and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                total += int(maps[nx][ny])
                
                answer.append(total)
    
    return sorted(answer) if answer else [-1]