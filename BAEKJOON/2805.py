import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

trees = list(map(int, input().strip().split()))

start, end = 0, max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2  
    total = 0

    
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    if total >= M:
        result = mid  # 현재 mid 높이를 기록
        start = mid + 1  # 더 큰 높이를 시도
    else:
        end = mid - 1  # 더 낮은 높이를 시도

# 결과 출력
print(result)
