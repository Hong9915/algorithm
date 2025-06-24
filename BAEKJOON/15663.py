import sys
input=sys.stdin.readline

N,M=map(int,input().strip().split())

array=sorted(list(map(int,input().strip().split())))
visited=[False]*N
x = set()
def dfs(M,index,array,visited,result=[]):
    
    if len(result)==M:
        if result not in x:
            x.add(tuple(result))
        return
    if index==len(array):
        return
    
    for i in range(len(array)):
        if not visited[i] :
            visited[i]=True
            dfs(M,index,array,visited,result+[array[i]])
            visited[i]=False
        
dfs(M,0,array,visited)

for rs in x:
    print(" ".join(map(str,rs)))