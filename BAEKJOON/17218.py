import sys
input = sys.stdin.readline

PASSWORD_1 = input().strip()
PASSWORD_2 = input().strip()

def longest_stirng(password_tag1,password_tag2):
    a,b=len(password_tag1),len(password_tag2)
    
    dp=[[" "]*(b+1) for _ in range(a+1)]
    
    for i in range(1,a+1):
        for j in range(1,b+1):
            if password_tag1[i-1]==password_tag2[j-1]:
                dp[i][j] = dp[i-1][j-1]+password_tag1[i-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1], key=len)
    
    return dp[a][b]

print(longest_stirng(PASSWORD_1,PASSWORD_2))