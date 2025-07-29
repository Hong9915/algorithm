from collections import defaultdict

def solution(info, n, m):
    dp=[[False]*n for _ in range(m)]
    dp[0][0]=True
    answer = n

    for a_trace, b_trace in info:
        next_dp = [[False] * n for _ in range(m)]
        for b in range(m):
            for a in range(n):
                if not dp[b][a]:
                    continue
                new_a = a + a_trace
                new_b = b
                if new_a < n and new_b < m:
                    next_dp[new_b][new_a] = True
                new_a = a
                new_b = b + b_trace
                if new_a < n and new_b < m:
                    next_dp[new_b][new_a] = True
        dp=next_dp
    
    for i in range(m):
        for j in range(n):
            if dp[i][j]==True:
                answer = min(answer, j)
    if answer != n:
        return answer
    
    return -1
