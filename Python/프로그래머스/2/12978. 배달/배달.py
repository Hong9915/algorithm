"""
먼저 road 순회하면서 각각 마을 별로 거리 defaultdict로 적용 1번부터 시작 heapq에 추가하면서 더짧은거있는지 확인 
"""
import heapq
from collections import defaultdict

def solution(N, road, K):
    distance = [float("inf")] * (N + 1)
    roads = defaultdict(list)
    answer = 0
    for st, en, cost in road:
        roads[st].append((en, cost))
        roads[en].append((st, cost))

    distance[1] = 0
    heap = [(0, 1)]  # 
    
    while heap :
        dis, cur = heapq.heappop(heap)
        if dis > distance[cur]:
            continue
        
        for en, cost in roads[cur]:
            if dis+cost <= distance[en]:
                heapq.heappush(heap,(dis+cost,en))
                distance[en] = dis+cost
    
    
    for dis in distance :
        if dis <= K:
            answer +=1
    return answer