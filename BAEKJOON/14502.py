import sys
from collections import deque
from itertools import combinations  # 조합을 위해 추가

def bfs():
    queue = deque()
    graph = [row[:] for row in matrix]  # deepcopy 없이 새로운 리스트 생성
    
    # 바이러스 위치 큐에 추가
    for x, y in virus_positions:
        queue.append((x, y))

    # 이동 방향 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):  # 네 방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 2  # 바이러스 확산
                queue.append((nx, ny))


    safe_area = sum(row.count(0) for row in graph)
    return safe_area  # 안전 영역 개수 반환

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())

    matrix = []
    empty_spaces = []  # 빈 칸 좌표 저장
    virus_positions = []  # 바이러스 좌표 저장

    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
        for j in range(M):
            if row[j] == 0:
                empty_spaces.append((i, j))  # 빈 칸 저장
            elif row[j] == 2:
                virus_positions.append((i, j))  # 바이러스 위치 저장

    result = 0  # 최대 안전 영역 크기

    # 빈 칸 중에서 3개를 고르는 조합을 생성
    for walls in combinations(empty_spaces, 3):
        # 벽 3개 세우기
        for x, y in walls:
            matrix[x][y] = 1

        # BFS 실행 후 최대값 갱신
        result = max(result, bfs())

        # 벽 원상복구
        for x, y in walls:
            matrix[x][y] = 0

    print(result)
