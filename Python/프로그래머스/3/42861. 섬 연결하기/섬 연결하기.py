import heapq

def solution(n, costs):
    graph = [[] for _ in range(n)]

    for a, b, cost in costs:
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    visited = [False] * n
    heap = [(0, 0)]
    answer = 0

    while heap:
        cost, now = heapq.heappop(heap)

        if visited[now]:
            continue

        visited[now] = True
        answer += cost

        for next_cost, next_node in graph[now]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_cost, next_node))

    return answer