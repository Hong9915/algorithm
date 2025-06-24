import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().strip().split())

def check(array, M, N, H):
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if array[h][n][m] == 0:
                    return False
    return True

def bfs(array, start_box, M, N, H):
    up = [1, -1, 0, 0, 0, 0]
    down = [0, 0, 1, -1, 0, 0]
    side = [0, 0, 0, 0, 1, -1]
    queue = deque(start_box)
    days = -1
    
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            
            for i in range(6):
                nx = x + up[i]
                ny = y + down[i]
                nz = z + side[i]
                
                if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and array[nz][ny][nx] == 0:
                    array[nz][ny][nx] = 1
                    queue.append((nx, ny, nz))
    
    if check(array, M, N, H):
        return days
    else:
        return -1

tomato_box = []
start_box = []

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(M):
            if row[m] == 1:
                start_box.append((m, n, h))
        layer.append(row)
    tomato_box.append(layer)

print(bfs(tomato_box, start_box, M, N, H))
