import sys
from collections import deque

input = sys.stdin.readline

def bfs(array, N):
    result = [[0] * N for _ in range(N)]  # 연결 관계를 저장할 결과 배열

    for i in range(N):
        visited = [False] * N  # 방문 여부를 체크하는 리스트
        queue = deque([i])  # BFS를 위한 큐 초기화

        while queue:
            node = queue.popleft()  # 큐에서 노드를 하나 꺼냄

            for j in range(N):
                if array[node][j] == 1 and not visited[j]:  # 연결되어 있고 아직 방문하지 않았다면
                    visited[j] = True  # 방문 표시
                    result[i][j] = 1  # 연결 관계 기록
                    queue.append(j)  # 큐에 추가하여 다음 탐색 대상으로 지정

    return result

N = int(input().strip())
array = []
for _ in range(N):
    array.append(list(map(int, input().strip().split())))

result = bfs(array, N)

for row in result:
    print(" ".join(map(str, row)))
