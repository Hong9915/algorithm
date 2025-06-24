from collections import deque

def bfs(N, M):
    if N == M:
        return 0, 1  # 시작 위치와 목표 위치가 같으면 거리 0, 경로 1개
    
    queue = deque([(N, 0)])  # (현재 위치, 거리)
    visited = [float('inf')] * 100001  # 방문 여부와 최단 거리 기록
    visited[N] = 0  # 시작 위치 방문 처리

    min_distance = float('inf')  # 최단 거리
    path_count = 0  # 최단 거리로 도달하는 경로 수

    while queue:
        current_step, current_distance = queue.popleft()

        if current_step == M:  
            if current_distance < min_distance:
                min_distance = current_distance
                path_count = 1  
            elif current_distance == min_distance:
                path_count += 1
            continue


        for next_step in (current_step - 1, current_step + 1, current_step * 2):
            if 0 <= next_step <= 100000:  
                if visited[next_step] >= current_distance + 1:
                    visited[next_step] = current_distance + 1
                    queue.append((next_step, current_distance + 1))

    return min_distance, path_count


import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())

distance,path=bfs(N,M)
print(distance)
print(path)