import sys

input=sys.stdin.readline

N=int(input())
Queen=[]
result=0
def check_queen(i : int ,j : int):
    for r,c in enumerate(Queen):
        if c == j or abs(r-i)==abs(c-j):
            return False
    return True

def solution(row):
    global result
    if row == N :
        result +=1
        return
    
    for col in range(N):
        if check_queen(row,col): #백트래킹
            Queen.append(col)
            solution(row+1)
            Queen.pop()
    
solution(0)
print(result)