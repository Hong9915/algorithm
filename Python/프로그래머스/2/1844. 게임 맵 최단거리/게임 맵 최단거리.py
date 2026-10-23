from collections import deque

def solution(maps):
    answer = 0
    
    m = len(maps)
    n = len(maps[0])
    
    queue = deque([(0,0,0)])
    visited = [[False] * (n+1) for _ in range(m+1)]
    visited[0][0] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while queue :
        cy, cx, cost = queue.popleft()
        
        if cy == m-1 and cx == n-1:
            return cost+1
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx] and maps[ny][nx] != 0:
                queue.append([ny,nx,cost+1])
                visited[ny][nx] = True
    
    
    return -1