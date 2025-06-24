import sys
import heapq

input = sys.stdin.readline

# 입력받기
N, M = map(int, input().strip().split())

graph = []
start = None

# 그래프 입력 및 목표 지점 찾기
for i in range(N):
    row = list(map(int, input().strip().split()))
    graph.append(row)
    if 2 in row:
        start = (i, row.index(2))

# 거리 배열 초기화
distances = [[-1] * M for _ in range(N)]  # -1로 초기화하여 도달 불가를 표시

def dijkstra(graph, start):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    distances[start[0]][start[1]] = 0  # 목표 지점의 거리는 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        x, y = current_node

        if current_distance > distances[x][y]:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 경계 체크 및 이동 가능한 경우
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:  # 갈 수 있는 땅
                    new_distance = current_distance + 1
                    if distances[nx][ny] == -1 or new_distance < distances[nx][ny]:
                        distances[nx][ny] = new_distance
                        heapq.heappush(priority_queue, (new_distance, (nx, ny)))
                elif graph[nx][ny] == 0:  # 갈 수 없는 땅
                    distances[nx][ny] = 0  # 갈 수 없는 땅은 0으로 설정

# Dijkstra 알고리즘 실행
dijkstra(graph, start)

# 결과 출력
for i in range(N):
    for j in range(M):
        # 갈 수 없는 땅(0)은 0으로 유지
        if graph[i][j] == 0:
            distances[i][j] = 0  # 갈 수 없는 땅은 0으로 설정
    print(' '.join(map(str, distances[i])))
