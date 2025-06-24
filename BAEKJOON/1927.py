import heapq
import sys

input = sys.stdin.readline

# 우선순위 큐 (최소 힙) 생성
min_heap = []

N = int(input().strip())

for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if min_heap:
            # 힙에서 최솟값 꺼내고 출력
            print(heapq.heappop(min_heap))
        else:
            # 힙이 비어있으면 0 출력
            print(0)
    else:
        # 힙에 원소 추가
        heapq.heappush(min_heap, x)
