import sys
input = sys.stdin.readline

TC = int(input())  

def bellman_ford(start, N):
    dist = {i: -1 for i in range(1, N + 1)}
    dist[start] = 0
    
    for _ in range(N - 1):
        for node in range(1, N + 1):
            for next_node, weight in room[node]:
                if dist[next_node] > dist[node] + weight:
                    dist[next_node] = dist[node] + weight
            print(dist)
    for node in range(1, N + 1):
        for next_node, weight in room[node]:
            if dist[next_node] > dist[node] + weight:
                return "YES"  

    return "NO"  

for _ in range(TC):
    N, M, W = map(int, input().strip().split())

    room = {i: [] for i in range(1, N + 1)}

    for _ in range(M):
        S, E, T = map(int, input().strip().split())
        room[S].append((E, T))
        room[E].append((S, T))  
   
    for _ in range(W):
        S, E, T = map(int, input().strip().split())
        room[S].append((E, -T)) 

    print(bellman_ford(1, N))
