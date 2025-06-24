import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  
M = int(input())  

def virus(start, graph):
    visited = set()  # 감염된 컴퓨터를 추적하기 위한 집합
    dq = deque([start])  # BFS를 위한 큐
    while dq:
        i = dq.popleft()
        if i not in visited:
            visited.add(i)
            for neighbor in graph[i]:
                if neighbor not in visited:
                    dq.append(neighbor)
    return visited


graph = {i: [] for i in range(1, N + 1)}

# 네트워크 연결 정보 입력
for _ in range(M):
    key, value = map(int, input().strip().split())
    graph[key].append(value)
    graph[value].append(key)

infected = virus(1, graph)
print(len(infected) - 1)  # 1번 컴퓨터를 제외한 감염된 컴퓨터 수
