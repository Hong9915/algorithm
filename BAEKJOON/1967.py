import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1): 
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def bfs(start: int):
    visited = set()
    queue = deque([(start, 0)]) 
    visited.add(start)
    farthest_node = start
    max_distance = 0

    while queue:
        node, dist = queue.popleft()

        if dist > max_distance:
            max_distance = dist
            farthest_node = node

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + weight))

    return farthest_node, max_distance

farthest_node, _ = bfs(1)

_, max_distance = bfs(farthest_node)

print(max_distance)
