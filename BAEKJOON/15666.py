import sys
input=sys.stdin.readline

N,M=map(int,input().strip().split())

array=sorted(list(map(int,input().strip().split())))
visited=[False]*N
x = set()
def dfs(M,index,array,result=[]):
    if len(result)==M:
        x.add(tuple(result))
        return
    if index==len(array):
        return
    

    
    dfs(M,index+1,array,result+[array[index]])
    dfs(M,index,array,result+[array[index]])
    dfs(M,index+1,array,result)
dfs(M,0,array)

for rs in sorted(x):
    print(" ".join(map(str,rs)))