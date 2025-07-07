def solution(board, h, w):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    answer = 0
    color=board[h][w]
    for i in range(4):
        cx,cy=w+dx[i],h+dy[i]
        if 0<=cx<len(board) and 0<=cy<len(board) and color==board[cy][cx]:
            answer+=1
    return answer