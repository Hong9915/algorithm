import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  # 매우 큰 값 (무한대)

def dijkstra(start):
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
    
    max_dist = max(distance[1:])  # 최댓값 찾기
    max_node = distance.index(max_dist)  # 가장 먼 노드 찾기
    return max_node, max_dist  # (노드, 거리) 반환

if __name__ == "__main__":
    N = int(input().strip())  # 정점 개수
    graph = [[] for _ in range(N + 1)]

    for _ in range(N):
        data = list(map(int, input().split()))
        node = data[0]
        index = 1
        
        while data[index] != -1:
            neighbor = data[index]
            weight = data[index + 1]
            graph[node].append((neighbor, weight))
            graph[neighbor].append((node, weight))  
            index += 2

    # 1. 아무 노드(예: 1번)에서 가장 먼 노드 찾기
    farthest_node, _ = dijkstra(1)
    
    # 2. 가장 먼 노드에서 다시 다익스트라 실행 → 트리의 지름 구하기
    _, tree_diameter = dijkstra(farthest_node)

    print(tree_diameter)  # 트리의 지름 출력
