import sys
from collections import deque

input = sys.stdin.readline

main_line = {}
N, M, V = map(int, input().strip().split())

for _ in range(M):
    key, value = map(int, input().strip().split())
    if key in main_line:
        main_line[key].append(value)
    else:
        main_line[key] = [value]

    if value in main_line:
        main_line[value].append(key)
    else:
        main_line[value] = [key]

for key in main_line:
    main_line[key].sort()

def bfs(dic, start):
    visited = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            if vertex in dic:
                for value in dic[vertex]:
                    if value not in visited:
                        queue.append(value)
    return visited

def dfs(dic, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if vertex in dic:
                for value in reversed(dic[vertex]):
                    if value not in visited:
                        stack.append(value)
    return visited

result_bfs = bfs(main_line, V)
result_dfs = dfs(main_line, V)

print(" ".join(map(str, result_dfs)))
print(" ".join(map(str, result_bfs)))
