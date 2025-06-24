import heapq

def find_middle_numbers(numbers):
    min_heap = []  # 작은 값들을 저장하는 최소 힙
    max_heap = []  # 큰 값들을 저장하는 최대 힙
    result = []

    for number in numbers:
        # 최대 힙에 삽입
        if not max_heap or number <= -max_heap[0]:
            heapq.heappush(max_heap, -number)
        else:
            heapq.heappush(min_heap, number)

        # 힙의 크기 조정
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        while len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 중간값 출력
        if len(max_heap) == len(min_heap):
            result.append(min(-max_heap[0], min_heap[0]))
        else:
            result.append(-max_heap[0])

    return result

if __name__ == "__main__":
    N = int(input())
    numbers = [int(input()) for _ in range(N)]

    result = find_middle_numbers(numbers)

    for res in result:
        print(res)
