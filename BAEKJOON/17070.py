#gpt

import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리
N = int(input())
Home = [list(map(int, input().split())) for _ in range(N)]

# 방향 정의: 가로(0), 세로(1), 대각선(2)
# 이동 방향 dx, dy: [가로, 세로, 대각선]
dx = [0, 1, 1]
dy = [1, 0, 1]
dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]
# 파이프 이동 가능한 경우 탐색
def find_the_way(x1, y1, x2, y2, state):
    if dp[x2][y2][state] != -1:
        return dp[x2][y2][state]
    if x2 == N - 1 and y2 == N - 1:  # 파이프가 (N, N)에 도달한 경우
        return 1
    total_ways = 0
    for next_state in range(3):  # 가로, 세로, 대각선
        if state == 0 and next_state == 1:  # 가로 → 세로 불가능
            continue
        if state == 1 and next_state == 0:  # 세로 → 가로 불가능
            continue

        nx1, ny1 = x2, y2
        nx2, ny2 = x2 + dx[next_state], y2 + dy[next_state]

        # 범위 확인 및 장애물 체크
        if 0 <= nx2 < N and 0 <= ny2 < N and Home[nx2][ny2] == 0:
            if next_state == 2:  # 대각선인 경우 추가로 확인
                if Home[nx1][ny2] == 1 or Home[nx2][ny1] == 1:
                    continue
            
            total_ways += find_the_way(nx1, ny1, nx2, ny2, next_state)
    dp[x2][y2][state] = total_ways
    return total_ways

# 초기 상태에서 탐색 시작
if Home[N - 1][N - 1] == 1:  # 목적지에 벽이 있는 경우
    print(0)
else:
    print(find_the_way(0, 0, 0, 1, 0))  # 초기 위치와 상태: (0, 1) 가로
