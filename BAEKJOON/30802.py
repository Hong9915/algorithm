import sys
import math
input=sys.stdin.readline

N=int(input().strip())# 회원수
N_size=list(map(int,input().strip().split()))
T,P=map(int,input().strip().split())

N_size=[math.ceil(x/T) for x in N_size]
T_shirt_sum=sum(N_size)
print(T_shirt_sum)

print(N//P,N%P,sep=" ")