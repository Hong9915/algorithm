import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().strip().split())

def check(array, M, N):
    for n in range(N):
        for m in range(M):
            if array[n][m] == 0:
                return False
    return True

def bfs(array, start_box, M, N):
    up = [1, -1, 0, 0]
    down = [0, 0, 1, -1]

    queue = deque(start_box)
    days = -1
    
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + up[i]
                ny = y + down[i]
                
                if 0 <= nx < M and 0 <= ny < N and array[ny][nx] == 0:
                    array[ny][nx] = 1
                    queue.append((nx, ny))
    
    if check(array, M, N):
        return days
    else:
        return -1

tomato_box = []
start_box = []


for n in range(N):
    row = list(map(int, input().split()))
    for m in range(M):
        if row[m] == 1:
            start_box.append((m, n))
    tomato_box.append(row)
if len(start_box)==M*N:
    print("0")
    exit()

print(bfs(tomato_box, start_box, M, N))
