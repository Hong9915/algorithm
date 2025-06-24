import sys
input=sys.stdin.readline

def find_subsequences(arr,index,M,combination=[]):
    if len(combination) == M:
        print(" ".join(map(str,combination)))
        return
    if index == len(arr):
        return
    find_subsequences(arr,index+1,M,combination+[arr[index]])
    find_subsequences(arr,index+1,M,combination)

N,M=map(int,input().strip().split())
arr=[x for x in range(1,N+1)]

        
find_subsequences(arr,0,M)

