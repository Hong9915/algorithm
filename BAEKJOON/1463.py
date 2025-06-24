#못품
import sys
input=sys.stdin.readline

N=int(input().strip())
#dp 테이블 초기화
d=[0]* 10000001

for i in range(2,N+1):
    #기본적으로 1을 빼는 연산을 통해 계산
    d[i]=d[i-1]+1
    
    if i%2==0:#2로 나누어 떨어지는 경우 원래보다 효율적인지 확인
        d[i]=min(d[i],d[i//2]+1)
    
    if i%3==0:#3로 나누어 떨어지는 경우 원래보다 효율적인지 확인
        d[i]=min(d[i],d[i//3]+1)


print(d[N])
