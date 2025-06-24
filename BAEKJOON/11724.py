import sys
from collections import deque

input = sys.stdin.readline

graph = {}
N, M = map(int, input().strip().split())

for _ in range(M):
    a, b = map(int, input().strip().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

def connected_component(graph, N):
    visited = [False] * (N + 1) 
    components = 0
    
    for i in range(1, N+1):
        if not visited[i]:
            components += 1
            queue = deque([i])
            visited[i] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph.get(node, []):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    return components

result = connected_component(graph, N)
print(result)
