import sys
input=sys.stdin.readline

N,M=map(int,input().strip().split())

array=sorted(list(map(int,input().strip().split())))
visited=[False]*10001
def dfs(M,index,array,visited,result=[]):
    
    if len(result)==M:
        print(" ".join(map(str,result)))
        return
    if index==len(array):
        return
    
    for i in array:
        if not visited[i]:
            visited[i]=True
            dfs(M,index,array,visited,result+[i])
            visited[i]=False
        
dfs(M,0,array,visited)