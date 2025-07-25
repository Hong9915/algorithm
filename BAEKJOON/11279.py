import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
heap = []

for _ in range(N):
    num = int(input().strip())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))  
    else:
        heapq.heappush(heap, -num)  