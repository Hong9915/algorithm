import sys
from collections import deque
input=sys.stdin.readline


visited=[-1]*101
N,M=map(int,input().strip().split())

def bfs(ladders,snails):
    queue=deque([1])
    visited[1]=0
    while queue:
        current= queue.popleft()
        for x in range(1,7,1):
            next=current+x
            if current+x > 100:
                continue
            if next in (ladders):
                next=ladders[next]
            if next in (snails):
                next=snails[next]
            
            if visited[next] == -1:
                if visited[next] > visited[current]+1:
                    queue.append(next)
                else:
                    visited[next]=(visited[current]+1)
                    queue.append(next)
            
            if next==100:
                return visited[next]
    return visited[next]
ladder={}
snail={}

for _ in range (N):
    a,b=map(int,input().strip().split())
    ladder[a]=b
for _ in range (M):
    a,b=map(int,input().strip().split())
    snail[a]=b
    
print(bfs(ladder,snail))
