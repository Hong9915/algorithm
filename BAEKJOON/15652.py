import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
array = [x for x in range(1, N + 1)]


def dfs(M, index, array, result=[]):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    
    if index==len(array):
        return
    
    dfs(M, index , array, result+[array[index]])
    dfs(M, index+1, array, result)
       


dfs(M, 0, array)
