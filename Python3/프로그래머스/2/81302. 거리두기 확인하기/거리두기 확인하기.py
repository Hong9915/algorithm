from collections import deque

def solution(places):
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def issafe(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P': # 위치 확인
                    q = deque()
                    q.append((i, j, 0))
                    visited = [[False] * 5 for _ in range(5)]
                    visited[i][j] = True

                    while q:
                        x, y, dist = q.popleft()
                        if dist >= 2: # 거리 초과시 통과
                            continue

                        for d in range(4):
                            nx, ny = x + dx[d], y + dy[d]
                            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                if place[nx][ny] == 'P':
                                    return False 
                                if place[nx][ny] == 'O':
                                    q.append((nx, ny, dist + 1))
        return True

    for place in places:
        if issafe(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer
