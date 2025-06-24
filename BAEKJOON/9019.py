from collections import deque

def D(n):
    return (2 * n) % 10000

def S(n):
    return 9999 if n == 0 else n - 1

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

def bfs(A, B):
    queue = deque([(A, '')])
    visited = [False] * 10000
    visited[A] = True
    
    while queue:
        current, operations = queue.popleft()
        
        if current == B:
            return operations
        
        # Apply the D operation
        next_num = D(current)
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, operations + 'D'))
        
        # Apply the S operation
        next_num = S(current)
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, operations + 'S'))
        
        # Apply the L operation
        next_num = L(current)
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, operations + 'L'))
        
        # Apply the R operation
        next_num = R(current)
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, operations + 'R'))
    
    return ""

T = int(input().strip())

for _ in range(T):
    A, B = map(int, input().strip().split())
    result = bfs(A, B)
    print(result)
