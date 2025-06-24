import sys
input = sys.stdin.readline

# 점의 개수 N을 입력받는다.
N = int(input())

# 점을 저장할 리스트를 초기화한다.
plane = []

# N개의 점을 입력받는다.
for _ in range(N):
    x, y = map(int, input().strip().split())
    plane.append((x, y))

# x좌표를 기준으로, x좌표가 같다면 y좌표를 기준으로 정렬한다.
plane.sort(key=lambda point: (point[1], point[0]))

# 정렬된 결과를 출력한다.
for x, y in plane:
    print(x, y)
