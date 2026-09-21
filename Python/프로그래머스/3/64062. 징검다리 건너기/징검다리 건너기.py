"""
전체 하나씩 1빼고 확인? ㅈㄴ 비효율적인데
모든 K구간중에 가장 큰값이 작은 곳을 가져오면 되네 heapq쓰고 sliding window 되면 딱 좋은데
"""
import heapq

def solution(stones, k):
    heap = []
    answer = []
    for i, value in enumerate(stones):
        heapq.heappush(heap,(-value,i))
        
        while heap[0][1] <= i-k : #인덱스가 i보다 작으면 삭제
            heapq.heappop(heap)
        
        if i >= k - 1 :
            answer.append(-heap[0][0])

    return min(answer)