import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
heap_positive = []  # 양수를 저장하는 최소 힙
heap_negative = []  # 음수의 절댓값을 저장하는 최소 힙 (최대 힙처럼 동작)

for _ in range(N):
    num = int(input().strip())
    if num == 0:
        if len(heap_positive) == 0 and len(heap_negative) == 0:
            print(0)
        else:
            if len(heap_negative) == 0:  # 음수 힙이 비어 있으면 양수 힙에서 pop
                print(heapq.heappop(heap_positive))
            elif len(heap_positive) == 0:  
                print(-heapq.heappop(heap_negative))
            else: 
                if heap_positive[0] < heap_negative[0]:
                    print(heapq.heappop(heap_positive))
                else:
                    print(-heapq.heappop(heap_negative))
    else:
        if num > 0:
            heapq.heappush(heap_positive, num)
        elif num < 0:
            heapq.heappush(heap_negative, -num)  # 음수는 절댓값으로 저장
