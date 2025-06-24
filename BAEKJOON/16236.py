import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
sea = []

# 바다 정보 입력받기
for i in range(N):
    row = list(map(int, input().strip().split())) 
    sea.append(row)
    if 9 in row:
        for j in range(N):
            if row[j] == 9:
                baby_shark = (i, j)  # 상어의 초기 위치

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_fish(shark, shark_size):
    distance = [[0] * N for _ in range(N)]  # 거리 배열
    visited = [[0] * N for _ in range(N)]  # 방문 배열
    queue = deque([(shark[0], shark[1])])
    visited[shark[0]][shark[1]] = 1
    temp = []
    
    while queue:
        c_shark_x, c_shark_y = queue.popleft()
        
        for i in range(4):
            n_shark_x = c_shark_x + dx[i]
            n_shark_y = c_shark_y + dy[i]
            
            if 0 <= n_shark_x < N and 0 <= n_shark_y < N and not visited[n_shark_x][n_shark_y] and sea[n_shark_x][n_shark_y] <= shark_size:
                distance[n_shark_x][n_shark_y] = distance[c_shark_x][c_shark_y] + 1
                visited[n_shark_x][n_shark_y] = 1  # 방문 처리
                queue.append((n_shark_x, n_shark_y))
                
                # 먹을 수 있는 물고기 찾기
                if sea[n_shark_x][n_shark_y] < shark_size and sea[n_shark_x][n_shark_y] != 0:
                    temp.append(((n_shark_x, n_shark_y), distance[n_shark_x][n_shark_y])) 
    
    if temp:
        temp.sort(key=lambda x: (x[1], x[0][0], x[0][1]))
        return temp[0]
    return None 

if __name__ == "__main__":
    shark_size = 2  # 상어 초기 크기
    total_distance = 0  # 총 이동 거리
    cnt = 0  # 먹은 물고기 수
    
    # 물고기 찾기 시작
    result = find_fish(baby_shark, shark_size)
    
    while result:  # 물고기가 있을 때만 계속해서 먹음
        total_distance += result[1]  # 거리 추가
        cnt += 1
        if cnt == shark_size:
            shark_size += 1  # 상어 크기 증가
            cnt = 0  # 먹은 물고기 수 초기화
        
        # 물고기 잡아먹은 위치를 0으로 업데이트
        sea[baby_shark[0]][baby_shark[1]]=0
        x, y = result[0]
        sea[x][y] = 0
        baby_shark=result[0]
        # 새로운 물고기 찾기
        result = find_fish(result[0], shark_size)
    
    print(total_distance)  # 총 이동 거리 출력
