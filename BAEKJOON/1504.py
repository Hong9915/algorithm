import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

# 정점(V), 간선(E) 입력받기
V, E = map(int, input().strip().split())

# 그래프 초기화
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # 무방향 그래프

# 목표 노드 v1, v2 입력받기
v1, v2 = map(int, input().strip().split())

# 다익스트라 함수 정의
def dijkstra(start):
    dist = {i: float('inf') for i in range(1, V + 1)}
    dist[start] = 0
    pq = [(0, start)]  # (누적 거리, 현재 노드)
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # 현재 노드까지의 최단 거리가 이미 더 짧다면 스킵
        if current_dist > dist[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist

# 다익스트라로 각 지점까지의 최단 거리 계산
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 가능한 두 경로 계산
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[V]  # 1 → v1 → v2 → V
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[V]  # 1 → v2 → v1 → V
# print(dist_from_1[V])
# 최종 결과 계산
result = dist_from_1[V]
# 출력
if result == float('inf'):
    print(-1)
else:
    print(result)
