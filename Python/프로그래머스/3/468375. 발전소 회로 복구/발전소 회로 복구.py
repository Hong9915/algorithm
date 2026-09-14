from collections import deque

def bfs_same_floor(grid, r1, c1, r2, c2):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque([(r1-1, c1-1, 0)])
    visited[r1-1][c1-1] = True
    while queue:
        cx, cy, time = queue.popleft()
        if cx == r2-1 and cy == c2-1:
            return time
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny, time + 1))
    return float('inf')

def calc_move_cost(grid, panels, panel1, panel2, elevator):
    f1, r1, c1 = panels[panel1]
    f2, r2, c2 = panels[panel2]
    er, ec = elevator
    floor_cost = abs(f1 - f2)
    if floor_cost == 0:
        return bfs_same_floor(grid, r1, c1, r2, c2)
    else:
        to_elevator   = bfs_same_floor(grid, r1, c1, er, ec)
        from_elevator = bfs_same_floor(grid, er, ec, r2, c2)
        return to_elevator + floor_cost + from_elevator

def solution(h, grid, panels, seqs):
    num_panel = len(panels)

    # 엘리베이터 위치
    elevator = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                elevator = (i+1, j+1)
                break

    # 패널 간 이동비용 미리 계산
    cost = [[0] * num_panel for _ in range(num_panel)]
    for i in range(num_panel):
        for j in range(num_panel):
            if i != j:
                cost[i][j] = calc_move_cost(grid, panels, i, j, elevator)

    # 선행 조건 비트마스크
    prereq_mask = [0] * num_panel
    for before, after in seqs:
        b, a = before-1, after-1
        prereq_mask[a] |= (1 << b)

    INF = float('inf')
    total_mask = (1 << num_panel) - 1

    dp = [[INF] * num_panel for _ in range(1 << num_panel)]
    dp[0][0] = 0 

    for mask in range(1 << num_panel):
        for cur in range(num_panel):
            if dp[mask][cur] == INF:
                continue

            # 다음 방문할 패널 (아직 활성화 안 된 것)
            for nxt in range(num_panel):
                if mask & (1 << nxt):  # 이미 활성화됨
                    continue
                # 선행 조건 체크
                if (prereq_mask[nxt] & mask) != prereq_mask[nxt]:
                    continue

                new_mask = mask | (1 << nxt)
                new_cost = dp[mask][cur] + cost[cur][nxt]
                if new_cost < dp[new_mask][nxt]:
                    dp[new_mask][nxt] = new_cost

    return min(dp[total_mask])