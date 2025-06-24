import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

array = list(map(int, input().strip().split()))

# 부분 합 배열 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + array[i - 1]

# 쿼리 처리
for _ in range(M):
    a, b = map(int, input().strip().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
