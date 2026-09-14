from collections import deque

def solution(land):
    N = len(land)
    M = len(land[0])
    column_sums = [0] * M
    visited = [[False]*M for _ in range(N)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for i in range(N):
        for j in range(M):
            if visited[i][j] or land[i][j] == 0:
                continue

            area = 1
            visited[i][j] = True
            queue = deque([(i, j)])
            columns = set([j])

            while queue:
                cx, cy = queue.popleft()
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        area += 1
                        columns.add(ny)

            for col in columns:
                column_sums[col] += area

    return max(column_sums)
