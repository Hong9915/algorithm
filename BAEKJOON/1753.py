import sys
import heapq
input = sys.stdin.readline


V, E = map(int, input().strip().split())
start = int(input())

graph = {i: [] for i in range(1, V + 1)}


for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))
    # graph[v].append((u, w))

def dij(start):
    dist = {i: float('inf') for i in range(1, V + 1)}
    dist[start] = 0
    pq = [(0, start)]  

    while pq:
        score, node = heapq.heappop(pq)
        # if dist[node] < score:
        #     continue

        for next_node, weight in graph[node]:
            if dist[next_node] > weight + score:
                dist[next_node] = weight + score
                heapq.heappush(pq, (dist[next_node], next_node))

    return dist

a = dij(start)

for i in range(1, V + 1):
    print(a[i] if a[i] != float('inf') else "INF")
