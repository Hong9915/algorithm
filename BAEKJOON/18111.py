import sys

input = sys.stdin.readline

N, M, B = map(int, input().strip().split())

# 블록 높이를 세기 위한 리스트
height_count = [0] * 257

# 높이 정보를 입력받고 세기
for _ in range(N):
    row = list(map(int, input().strip().split()))
    for h in row:
        height_count[h] += 1

min_time = float('inf')  # 최소 시간을 무한대로 초기화
best_height = 0          # 최적의 높이

# 현재 인벤토리 블록 수
current_inventory = B

# 전체 블록 수를 계산
total_blocks = sum(height_count)

# 목표 높이 범위에 대해 반복
for target_height in range(257):
    time = 0
    blocks_needed = 0  # 현재 높이에서 필요한 블록 수
    
    for h in range(257):
        if h < target_height:
            blocks_needed += height_count[h] * (target_height - h)  # 필요한 블록 수
            time += height_count[h] * (target_height - h)  # 추가 시간 1초
        elif h > target_height:
            blocks_needed -= height_count[h] * (h - target_height)  # 제거할 블록 수
            time += height_count[h] * (h - target_height) * 2  # 제거 시간 2초

    # 인벤토리에 블록이 충분한 경우
    if blocks_needed <= current_inventory:
        if time < min_time:
            min_time = time
            best_height = target_height
        elif time == min_time and target_height > best_height:
            best_height = target_height

print(min_time, best_height)
