import sys
from collections import deque


input = sys.stdin.readline
N = int(input())  
graph = [[] for _ in range(N+1)]  

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


result = [0] * (N + 1) 

def bfs(start):
    queue=deque()
    queue.append(start)
    while(queue):
        x=queue.popleft()
        for i in graph[x]:
            if result[i]==0:
                queue.append(i)
                result[i]=x
            else: continue
bfs(1)
for i in range(2, N+1):
    print(result[i])
