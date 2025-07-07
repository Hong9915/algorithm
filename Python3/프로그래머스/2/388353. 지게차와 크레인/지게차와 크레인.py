from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def solution(storage, requests):
    def bfs_update():  
        visited = [[False] * M for _ in range(N)]
        q = deque()
        q.append((0, 0))
        visited[0][0] = True

        while q:
            y, x = q.popleft()
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    if graph[ny][nx] == '0':
                        visited[ny][nx] = True
                        q.append((ny, nx))
                    elif graph[ny][nx] == '1':
                        visited[ny][nx] = True
                        graph[ny][nx] = '0'
                        q.append((ny, nx))

    N = len(storage) + 2  
    M = len(storage[0]) + 2  


    graph = [['0'] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            graph[i][j] = storage[i - 1][j - 1]

    for req in requests:
        target = req[0]

        if len(req) == 1:
            to_remove = []
            for i in range(1, N - 1):
                for j in range(1, M - 1):
                    if graph[i][j] == target:
                        for d in range(4):
                            ni, nj = i + dy[d], j + dx[d]
                            if graph[ni][nj] == '0':
                                to_remove.append((i, j))
                                break
            for i, j in to_remove:
                graph[i][j] = '0'
            bfs_update()

        else:  
            for i in range(1, N - 1):
                for j in range(1, M - 1):
                    if graph[i][j] == target:
                        graph[i][j] = '1' 
            bfs_update()

    remaining = sum(1 for i in range(1, N - 1) for j in range(1, M - 1)
                    if graph[i][j] not in ('0', '1'))
    return remaining
