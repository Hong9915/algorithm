import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

cities = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().strip().split())
    cities[A].append((B, C))

start, end = map(int, input().strip().split())

def dijkstra(graph, start):
    INF = float('inf')
    distance = [INF] * (N + 1)
    distance_trace = [[] for _ in range(N + 1)]

    distance[start] = 0
    distance_trace[start] = [start]
    
    pq = [(0, start)]
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if dist > distance[node]:
            continue
        
        for nx, di in graph[node]:
            weight = di + dist
            if distance[nx] > weight:
                distance[nx] = weight
                distance_trace[nx] = distance_trace[node] + [nx] 
                heapq.heappush(pq, (weight, nx))
    
    return distance, distance_trace

distance, path = dijkstra(cities, start)


print(distance[end])

print(len(path[end])) 
print(*path[end])  