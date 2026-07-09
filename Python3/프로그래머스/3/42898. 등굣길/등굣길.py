"""
bfs해서 최단 거리 하나 구하고
다시 bfs해서 최단거리 된것들을 센후 1000000007로 나누기?
"""
def solution(m, n, puddles):
    set_puddles = {(y,x) for x,y in puddles}
    dp = [[0] * (m+1) for _ in range(n+1)]
    MOD = 1_000_000_007
    dp[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i== 1 and j==1:
                continue
            if (i,j) in set_puddles:
                continue
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])% MOD
    
    return dp[n][m]