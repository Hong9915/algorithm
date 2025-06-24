import sys

input = sys.stdin.readline

# 입력 받기
R, C, T = map(int, input().strip().split())

room = []
air_conditioner = []

for i in range(R):
    x = list(map(int, input().strip().split()))
    for j in range(C):
        if x[j] == -1:
            air_conditioner.append(i)  
    room.append(x)

dx = [0, 0, 1, -1]  
dy = [1, -1, 0, 0]

def spread_dust():
    global room
    new_room = [[0] * C for _ in range(R)]
    
    for a in air_conditioner:
        new_room[a][0] = -1

    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                spread_amount = room[i][j] // 5
                spread_count = 0

                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        new_room[nx][ny] += spread_amount
                        spread_count += 1

                new_room[i][j] += room[i][j] - (spread_amount * spread_count)

    room = new_room  

def move_upper():
    upper = air_conditioner[0]
    room[upper+1][0]=0
    # 아래쪽으로 이동
    for i in range(upper - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    # 왼쪽으로 이동
    for i in range(C - 1):
        room[0][i] = room[0][i + 1]
    # 위쪽으로 이동
    for i in range(upper):
        room[i][C - 1] = room[i + 1][C - 1]
    # 오른쪽으로 이동
    for i in range(C - 1, 1, -1):
        room[upper][i] = room[upper][i - 1]
    room[upper][1] = 0  # 공기청정기에서 나오는 바람

# 아래쪽 공기청정기 작동 (시계 방향)
def move_lower():
    lower = air_conditioner[1]
    room[lower-1][0]=0
    # 위쪽으로 이동
    for i in range(lower + 1, R - 1):
        room[i][0] = room[i + 1][0]
    # 왼쪽으로 이동
    for i in range(C - 1):
        room[R - 1][i] = room[R - 1][i + 1]
    # 아래쪽으로 이동
    for i in range(R - 1, lower, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    # 오른쪽으로 이동
    for i in range(C - 1, 1, -1):
        room[lower][i] = room[lower][i - 1]
    room[lower][1] = 0  # 공기청정기에서 나오는 바람

# T초 동안 실행
for _ in range(T):
    spread_dust()  # 미세먼지 확산
    move_upper()   # 위쪽 공기청정기 작동
    move_lower()   # 아래쪽 공기청정기 작동

# 남아있는 미세먼지 양 계산
result = sum(sum(row) for row in room if sum(row) > 0)
print(result)
