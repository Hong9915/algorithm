#진짜 ㅅㅂ왜 초과되는지 모르겠어요
from collections import deque

dr = (-1,1,0,0)
dc = (0,0,-1,1)

def bfs():
    visited = [[float('inf')] * W for _ in range(H)]# 길이가 W 높이가 H 인 2차원 배열 생성 초기 원소 값은 'inf'무한대로 초기화
    visited[sr][sc] = -1 #sr,sc 는 시작 지점 시작 지점은 -1로 함
    Q = deque([(sr,sc)])#시작 지점을 빼옴
    while Q:
        r, c = Q.popleft()# 시작 지머을 가져옴
        if (r,c) == (gr,gc) : #종료조건 만나게되면 값을 리턴시킴
            return visited[gr][gc]
        
        for i in range(4):
            nr = r + dr[i] #동서남북 방향으로
            nc = c + dc[i]
            while True :
                if not (0 <= nr < H and 0 <= nc < W): # 범위를 넘게되면 나가기
                    break
                if MAP[nr][nc] == "*": #벽을 만나면 나가기
                    break
                if visited[nr][nc] < visited[r][c] + 1: #지금 방문되는 위치에서 사용된 거울갯수가 지금+1 보다 크다면 멈추기 의미가 없음 
                    break
                Q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
                nr += dr[i]
                nc += dc[i]

if __name__ == "__main__" :
    W, H = map(int,input().split())
    MAP, C = [],[]
    sr , sc , gr , gc = 0,0,0,0
    for i in range (H):
        MAP.append(list(input().strip()))
        for j in range (W):
            if MAP[i][j] == "C":
                C.append((i,j))

    (sr,sc),(gr,gc) = C

    
    print(bfs())
