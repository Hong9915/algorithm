import sys

input=sys.stdin.readline

N=int(input().strip())

x=[0]*1001
x[1]=1
x[2]=2
for i in range(3,N+1):
    x[i]=(x[i-1]+x[i-2])% 10007
    
print(x[N]) 