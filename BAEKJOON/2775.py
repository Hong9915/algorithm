# T=int(input())

# def find_people(a,b):
#     if a==0:
#         return b
#     _sum=0
#     for j in range(1,b+1):
#         _sum+=find_people(a-1,j)
#     return _sum

# for _ in range(T):
#     k= int(input())
#     n= int(input())
#     print(find_people(k,n))

#
import sys
input = sys.stdin.readline

T = int(input())
results = []
dp=[]
for _ in range(T):
    k = int(input())
    n = int(input())
    
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(n + 1):
        dp[0][i] = i
    
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    
    results.append(dp[k][n])

# Print all results
for result in results:
    print(result)
