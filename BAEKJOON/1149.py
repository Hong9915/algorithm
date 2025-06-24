import sys
input=sys.stdin.readline

N=int(input())
House_cost=[]
for _ in range(N):
    row=list(map(int,input().strip().split()))
    House_cost.append(row)
visited=[[0]*3 for _ in range(N)]

def dp(cost,visited):

    visited[0][0],visited[0][1],visited[0][2]=cost[0][0],cost[0][1],cost[0][2]
    
    for i in range(1,N):
        visited[i][0]=min(visited[i-1][1]+cost[i][0],visited[i-1][2]+cost[i][0])
        visited[i][1]=min(visited[i-1][0]+cost[i][1],visited[i-1][2]+cost[i][1])
        visited[i][2]=min(visited[i-1][0]+cost[i][2],visited[i-1][1]+cost[i][2])
    
    return min(visited[N-1])

print(dp(House_cost,visited))