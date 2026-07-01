import heapq

def solution(A, B):
    heapq.heapify(A)           

    B = [-b for b in B]        
    heapq.heapify(B)

    answer = 0

    while A:
        min_a = heapq.heappop(A)
        max_b = -heapq.heappop(B)

        answer += min_a * max_b

    return answer