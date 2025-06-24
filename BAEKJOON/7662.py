#못품
import heapq
import sys

input = sys.stdin.readline

def dual_priority_queue(k, operations):
    min_heap = []
    max_heap = []
    deleted = {}

    for operation in operations:
        command, num = operation.split()
        num = int(num)

        if command == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in deleted:
                deleted[num] += 1
            else:
                deleted[num] = 1
        
        elif command == 'D':
            if num == 1:  # 최대값 삭제
                while max_heap and deleted[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)  # 유효하지 않은 값 제거
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    deleted[max_val] -= 1
            elif num == -1:  # 최소값 삭제
                while min_heap and deleted[min_heap[0]] == 0:
                    heapq.heappop(min_heap)  # 유효하지 않은 값 제거
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    deleted[min_val] -= 1
    
    # 유효한 최댓값과 최솟값 찾기
    while max_heap and deleted[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and deleted[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")

# 입력 처리
T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    operations = [input().strip() for _ in range(k)]
    dual_priority_queue(k, operations)
