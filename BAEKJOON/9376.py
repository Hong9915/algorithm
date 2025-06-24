import sys 
from collections import deque #
input = sys.stdin.readline # 파이썬에서 표준 입력(stdin)을 읽어오는 함수로 sys.stdin.readline을 input에 할당하는 것입니다. sys.stdin.readline은 표준 입력에서 한 줄씩 문자열을 읽어오는 함수입니다.

testCase = int(input()) # testcase 갯수
for _ in range(testCase):
    h, w = map(int, input().split()) #가로 세로 입력받기

    # 상근이의 위치를 특정화 하기 어렵기 때문에 graph의 상화좌우에 빈칸을 더해준다.
    graph = [["." for _ in range(w+2)]] #graph 맨위에 한줄 추가
    for y in range(h): # 높이 만큼
        row = list(input()[:-1])#row = list(input()[:-1]): 입력받은 문자열의 마지막에 있는 개행 문자(\n)를 제외하고, 각 행을 리스트로 변환합니다. 이 리스트 row는 현재 행에 대한 정보를 담고 있습니다.
        graph.append(["."] + row + ["."]) #row 앞뒤로 빈칸 더하기
    graph.append(["." for _ in range(w+2)])#graph 맨아래에 한줄 추가
    # for i in range(h):
    #     print(graph[i], "\n")
    dx = [0,0,-1,1] # 좌우 좌표 이동
    dy = [-1,1,0,0] # 상하 좌표 이동

    # y, x에서 출발했을 때 각 지점까지 문을 얼마나 열고 가야하는 지 값 출력
    def bfs(y, x):
        dq = deque([(y, x)]) #시작점을 가지고 있는 덱을 생성
        dist = [[-1 for _ in range(w+2)] for _ in range(h+2)] #시작점으로부터 각 점까지의 거리를 저장하는 이차원 리스트 'dist'를 생성합니다 초기에는 모든 점까지의 거리를 '-1'로 초기화합니다.
        dist[y][x] = 0 #시작점의 거리를 '0'으로 설정
        while dq: #덱이 비어 있지 않을 때까지
            y, x = dq.pop() #덱 오른쪽에서 좌표를 하나 꺼내옴
            for d in range(4): #4번 반복하여 상하좌우로 이동
                nx = x + dx[d] 
                ny = y + dy[d]
                if 0 <= nx < w+2 and 0 <= ny < h+2 and graph[ny][nx] != "*" and dist[ny][nx] == -1: # ny, nx graph범위를 넘지 않고 벽에 부딪히지 않고 아직 방문하지 않은 곳이라면 실행
                    if graph[ny][nx] == "#": # 만약 새로운 위치가 문이라면
                        dist[ny][nx] = dist[y][x] + 1 #새로운 위치가 현재위치보다 거리가 1 높다고 설정(문을 열었다랑 같은 말)
                        dq.appendleft((ny, nx)) #덱의 왼쪽에 문위치를 추가함
                    else:
                        dist[ny][nx] = dist[y][x] #아니라면 위치를 변환
                        dq.append((ny, nx)) #덱의 오른쪽에 위치를 변환

        return dist
    # 수감자 위치 찾기
    prisoner = []
    for y, row in enumerate(graph): #각행에 대하여 순회함
        for x, v in enumerate(row):#순회중인 각행을 순회함
            if v == "$":#수감자 위치를 찾아냄
                prisoner.append((y, x))

    # 수감자들의 위치와 상근이 위치에서 각각 bfs를 돌려준다.   
    dist1 = bfs(prisoner[0][0], prisoner[0][1]) #첫번째 수감자 위치
    dist2 = bfs(prisoner[1][0], prisoner[1][1]) #두번째 수감자 위치
    dist3 = bfs(0,0) #수감자가 밖을 찾지 못하는 경우를 계산하기 위해가 아닌가?
    # 합이 최소가 되는 값을 찾는다. 단, 위치가 문이라면 -2를 해준다.
    result = float("inf")
    for y in range(h+2):
        for x in range(w+2):
            s = dist1[y][x] + dist2[y][x] + dist3[y][x] 
            if graph[y][x] == "#":
                s -= 2
            if s >= 0:
                result = min(result, s)

    print(result)