# #못품
import sys
from collections import deque

# def find_the_fastest_time(subin, brother):
#     if subin >= brother:# 수빈이 더 클떄는 -1한만큼
#         return subin - brother
    
#     max_position = 100000
#     visited = [False] * (max_position + 1)
#     queue = deque([(subin, 0)])  # (현재 위치, 시간)
    
#     while queue:
#         current, time = queue.popleft()
        
#         if current == brother:
#             return time
        
#         # 가능한 이동: 현재 위치 -1, 현재 위치 +1, 현재 위치 * 2
#         for next_position in (current - 1, current + 1, current * 2):
#             if 0 <= next_position <= max_position and not visited[next_position]:
#                 visited[next_position] = True
#                 queue.append((next_position, time + 1))

# # 입력 받기
# N, K = map(int, sys.stdin.readline().strip().split())

# # 결과 출력
# print(find_the_fastest_time(N, K))


N, K = map(int, input().strip().split())

def find_fastest_way(N, K):
    if N>=K:
        return N-K
    queue = deque()
    queue.append((N, 0))  
    visited = [False] * 100001  
    
    while queue:
        now, time = queue.popleft() 
        if now == K:  
            return time
        visited[now] = True  

        for next_step in [now - 1, now + 1, now * 2]:
            if 0 <= next_step < 100001 and not visited[next_step]:  
                queue.append((next_step, time + 1))  

print(find_fastest_way(N, K))
