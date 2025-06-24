import sys
input = sys.stdin.readline

first_string = input().strip()
second_string = input().strip()

n = len(first_string)
m = len(second_string)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if first_string[i-1]==second_string[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[n][m])