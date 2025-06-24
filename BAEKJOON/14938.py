import sys

# 입력 받기
n, m, r = map(int, input().strip().split())
items = list(map(int, input().strip().split()))


INF = sys.maxsize
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0


for _ in range(r):
    a, b, l = map(int, input().strip().split())
    a -= 1
    b -= 1
    dist[a][b] = l
    dist[b][a] = l


for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 최대 아이템 개수 계산
max_items = 0
for i in range(n):
    total_items = sum(items[j] for j in range(n) if dist[i][j] <= m)
    max_items = max(max_items, total_items)

print(max_items)