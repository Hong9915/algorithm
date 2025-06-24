import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().strip().split())

def bfs(A, B):
    queue = deque([(A, 1)])  #
    visited = set()  
    
    while queue:
        num, count = queue.popleft()
        
        if num == B:  
            return count
        
        if num > B:  
            continue

        if num * 2 not in visited:
            visited.add(num * 2)
            queue.append((num * 2, count + 1))
        
        if num * 10 + 1 not in visited:
            visited.add(num * 10 + 1)
            queue.append((num * 10 + 1, count + 1))
    
    return -1  
# BFS 실행
result = bfs(A, B)
print(result)
