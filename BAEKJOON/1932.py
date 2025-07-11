import sys
input=sys.stdin.readline

N=int(input().strip())
triangle = [list(map(int, input().strip().split())) for _ in range(N)]

dp=[[0]*N for _ in range(N)]
dp[0][0]=triangle[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j==0:
            dp[i][j]=dp[i-1][j]+triangle[i][j]
        elif i==j:
            dp[i][j]=dp[i-1][j-1]+triangle[i][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
temp=dp[N-1]

print(max(temp))