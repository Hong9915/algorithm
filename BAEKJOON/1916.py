import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input().strip())

class City:
    def __init__(self):
        self.connect_city = [[] for _ in range(N + 1)]  

    def add_road(self, A, B, cost):
        self.connect_city[A].append((B, cost))
city = City()
for _ in range(M):
    A, B, cost = map(int, input().strip().split())
    city.add_road(A, B, cost)

X, Y = map(int, input().strip().split())

def dijkstra(start, end, city):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]  

    while queue:
        current_cost, current_city = heapq.heappop(queue)

        if current_cost > distances[current_city]:
            continue

        for next_city, road_cost in city.connect_city[current_city]:
            new_cost = current_cost + road_cost
            if new_cost < distances[next_city]:
                distances[next_city] = new_cost
                heapq.heappush(queue, (new_cost, next_city))

    return distances[end] if distances[end] != float('inf') else -1  

result = dijkstra(X, Y, city)
print(result)
