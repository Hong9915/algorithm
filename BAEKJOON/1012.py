import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y, M, N, lst, visited):  # DFS 함수를 추가하여 연결된 그룹 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < M and 0 <= ny < N and lst[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny, M, N, lst, visited)

def count_insect(lst, M, N):
    count = 0
    visited = [[False] * N for _ in range(M)]  # 방문 체크 배열 추가
    
    for i in range(M):
        for j in range(N):
            if lst[i][j] == 1 and not visited[i][j]:
                dfs(i, j, M, N, lst, visited)
                count += 1
    
    return count

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().strip().split())
    ground = [[0] * N for _ in range(M)]
    
    for _ in range(K):
        x, y = map(int, input().strip().split())
        ground[x][y] = 1
    
    print(count_insect(ground, M, N))
