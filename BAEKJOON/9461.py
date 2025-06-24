import sys
input=sys.stdin.readline

T=int(input().strip())

def pado(N):
    sequence=[0]*(N+1)
    for i in range(N+1):
        if i < 4:
            sequence[i]=1
            continue
        elif i < 6:
            sequence[i]=2
            continue
        sequence[i]=sequence[i-1]+sequence[i-5]
    return sequence[N]
for _ in range(T):
    N=int(input().strip())
    print(pado(N))
    