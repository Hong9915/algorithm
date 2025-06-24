import sys
input = sys.stdin.readline

# 상하좌우 이동 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global max_count
    max_count = max(max_count, count)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny]) - 65]:
            visited[ord(board[nx][ny]) - 65] = True
            dfs(nx, ny, count + 1)
            visited[ord(board[nx][ny]) - 65] = False

# 입력 처리
R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

# 최대 칸 수 초기화
max_count = 0

visited = [False] * 26
visited[ord(board[0][0]) - 65] = True

# DFS 탐색 시작
dfs(0, 0, 1)

# 결과 출력
print(max_count)
