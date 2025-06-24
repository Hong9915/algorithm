import sys

input= sys.stdin.readline
steps=[]
N=int(input().strip())
for _ in range(N):
    steps.append(int(input()))
dq=[0]*(N)

if N==1:
    print(steps[0])
    exit()
    
elif N==2:
    print(steps[0]+steps[1])
    exit()
    
dq[0]=steps[0]
dq[1]=steps[0]+steps[1]

for i in range(2,N):
    dq[i]=max(dq[i-2]+steps[i],steps[i-1]+dq[i-3]+steps[i])

print(dq[-1])