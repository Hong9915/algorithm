import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한대 값

def dijkstra(start, N, graph):
    distance = [INF] * (N + 1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        dist, now = heapq.heappop(pq)
        
        if distance[now] < dist:
            continue
        
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:  # 더 짧은 거리 발견하면 갱신
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    
    return distance  # start 노드에서 모든 노드까지의 최단 거리 반환

if __name__ == "__main__":
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]  # 그래프 초기화
    reverse_graph = [[] for _ in range(N + 1)]  # 역방향 그래프 (돌아오는 길)

    # 도로 정보 입력받기
    for _ in range(M):
        start, finish, time = map(int, input().split())
        graph[start].append((finish, time))  # 일반 그래프
        reverse_graph[finish].append((start, time))  # 역방향 그래프

    # 1. X번 마을에서 모든 마을로 가는 최단 거리 계산
    to_X = dijkstra(X, N, reverse_graph)

    # 2. 모든 마을에서 X번 마을로 가는 최단 거리 계산
    from_X = dijkstra(X, N, graph)

    max_time = 0
    for i in range(1, N + 1):
        # i번 마을에서 X로 가고 X에서 다시 i번 마을로 돌아오는 시간 계산
        round_trip = from_X[i] + to_X[i]
        max_time = max(max_time, round_trip)  # 가장 많이 걸리는 시간 갱신

    print(max_time)
