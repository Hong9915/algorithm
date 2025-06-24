from collections import deque
import sys

# 입력 속도 향상을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 상하좌우 이동을 위한 좌표 변화
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 백조의 이동을 BFS로 확인하는 함수
def check_swans_meet():
    while queue_swans:#백조 시작위치
        x, y = queue_swans.popleft()
        if x == target_x and y == target_y:#백조 위치가 목표위치에 도달되면 도달되었다고 리턴함
            return 1
        for i in range(4): #각방향으로 4번 반복함
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols: 
                if not visited[nx][ny]:#백조가 방문된 곳이 아니라면
                    if lake[nx][ny] == '.': # 백조가 움직인 곳이 물이라면
                        queue_swans.append([nx, ny]) #백조(큐)에 위치를 넣음
                    else:
                        temp_queue_swans.append([nx, ny]) # 백조가 움직인 곳이 얼음이라면 임시 백조(큐)에 넣음
                    visited[nx][ny] = 1 #방문된곳이라고 설정
    return 0

# 얼음을 녹이는 함수
def melt_ice():
    while water_queue: #물(큐)안에는 백조랑 물 위치가 저장되어있음
        x, y = water_queue.popleft() #하나씩 왼쪽부터 꺼내서 x좌표 y좌표를 저장함
        if lake[x][y] == 'X': #호수에 좌표가 얼음으로 표시되어있으면 물로 바꿈
            lake[x][y] = '.'
        for i in range(4): #위옆아래위방햑으로 4번반복함
            nx = x + dx[i] # i=0일때 x좌표 우측으로한칸 i=1일때 x좌표 좌측으로 한칸
            ny = y + dy[i] # i=2일때 y좌표 위로한칸 i=3일때 y좌표 아래로 한칸
            if 0 <= nx < rows and 0 <= ny < cols: #nx, ny가 가로,세로 값을 넘어가지 않을떄
                if not water_visited[nx][ny]: # not은 water_visited가 0일때임 방문되지 않았을때
                    if lake[nx][ny] == 'X': # 방문되지 않은 위치일때 호수가 얼음 상태라면 
                        temp_water_queue.append([nx, ny]) #임시 물 (큐)에 위치를 넣음
                    else:
                        water_queue.append([nx, ny]) # 얼음이 아니라면 물 (큐)에 넣음
                    water_visited[nx][ny] = 1 # 방문된 상태로 표시

# 입력 받기
rows, cols = map(int, input().split()) # 세로, 가로 값 입력 받기
visited = [[0] * cols for _ in range(rows)] # 방문된곳 입력 초기화 상태
water_visited = [[0] * cols for _ in range(rows)] # 물이 방문한곳 초기화
lake, initial_swans = [], [] # 호수, 초기 백조 위치
queue_swans, temp_queue_swans, water_queue, temp_water_queue = deque(), deque(), deque(), deque() # 4개 디큐 만들기

# 호수의 초기 상태 입력받기
for i in range(rows): #세로 값 만큼 반복
    row = list(input().strip()) #세로에 입력되는 곳 입력
    lake.append(row) # 한 줄이 끝나면 호수에 저장
    for j, k in enumerate(row): # enumerate 는 index 와 원소로 이루어진 tuple 상태로 만들어줌
        if lake[i][j] == 'L': #백조 위치 찾아서 초기 백조 위치에 저장하고   
            initial_swans.extend([i, j]) #extend는 리스트 자체를 리스트 안에 넣음
            water_queue.append([i, j])#append는 리스트에 추가시킴 i,j 원소를 넣음 , 물(큐)안에 백조위치를 넣음
        elif lake[i][j] == '.':
            water_visited[i][j] = 1 # 방문한 물에 1을 추가함
            water_queue.append([i, j])#물(큐)안에 물 위치를 넣음

# 백조의 초기 위치 및 큐 초기화
start_x, start_y, target_x, target_y = initial_swans # 백조 위치 저장
queue_swans.append([start_x, start_y]) #시작 백조 위치를 백조(큐)안에 저장
lake[start_x][start_y], lake[target_x][target_y], visited[start_x][start_y] = '.', '.', 1 # 호수 백조 위치를 물로 바꾸고 시작 백초 위치를 1로 바꿈
days_count = 0 #날짜 초기화

# 두 백조가 만날 때까지 반복
while True:
    print(*lake, sep= ', \n')
    print("queue_swans =", queue_swans)
    print("water_swans =", water_queue)
    print("temp_queue_swans=", temp_queue_swans)
    print("temp_water_queue=", temp_water_queue) 
    melt_ice() # 얼음 녹이기
    if check_swans_meet():
        print(days_count)
        break
    
    queue_swans, water_queue = temp_queue_swans, temp_water_queue
    temp_queue_swans, temp_water_queue = deque(), deque()
    days_count += 1
