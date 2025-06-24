def dfs(x, y):
    # 방향 벡터: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 스택을 이용한 DFS
    stack = [(x, y)]
    count = 0
    
    while stack:
        cx, cy = stack.pop()
        if not visited[cx][cy]:
            visited[cx][cy] = True
            count += 1
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 1:
                    stack.append((nx, ny))
    
    return count


# 입력 처리
N = int(input().strip())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 단지 정보 수집
complex_sizes = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            size = dfs(i, j)
            complex_sizes.append(size)

# 결과 출력
complex_sizes.sort()
print(len(complex_sizes))
for size in complex_sizes:
    print(size)
