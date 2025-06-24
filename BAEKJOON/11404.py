import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

# 입력 처리
N = int(input().strip())  # 도시의 수
M = int(input().strip())  # 버스 정보의 수

# 그래프 초기화
graph = [[] for _ in range(N)]
for _ in range(M):
    start, end, cost = map(int, input().strip().split())
    graph[start - 1].append((end - 1, cost))  # 0-based indexing

# 다익스트라 함수 정의
def dijkstra(start):
    dist = [INF] * N
    dist[start] = 0
    pq = [(0, start)]  # (거리, 노드) 우선순위 큐
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        print(current_dist,current_node)
        if current_dist > dist[current_node]:
            continue
        for neighbor, cost in graph[current_node]:
            new_dist = current_dist + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist

# 모든 출발점에 대해 다익스트라 실행
result = []
for i in range(N):
    result.append(dijkstra(i))

# 결과 출력
for i in range(N):
    for j in range(N):
        if result[i][j] == INF:
            print(0, end=" ")  # 도달할 수 없는 경우 0 출력
        else:
            print(result[i][j], end=" ")
    print()
