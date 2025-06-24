import sys
input = sys.stdin.readline

maximum = 0

N, M = map(int, input().strip().split())

visited = [[False] * M for _ in range(N)]


def dfs(x, y, arrays, tmp, cnt):
    global maximum
    if cnt == 4:
        maximum = max(maximum, tmp)
        return
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, arrays, tmp + arrays[nx][ny], cnt + 1)
            visited[nx][ny] = False


def check_t_shape(x, y, arrays):
    global maximum
    sum_val = arrays[x][y]
    min_block = float('inf')
    block_count = 0
    total_sum = sum_val
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            block_count += 1
            total_sum += arrays[nx][ny]
            min_block = min(min_block, arrays[nx][ny])
    
    if block_count == 4:
        total_sum -= min_block
    elif block_count < 3:
        return
    
    maximum = max(maximum, total_sum)


arrays = []
for _ in range(N):
    arrays.append(list(map(int, input().strip().split())))

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, arrays, arrays[i][j], 1)
        visited[i][j] = False
        check_t_shape(i, j, arrays)

print(maximum)
