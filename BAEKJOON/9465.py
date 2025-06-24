import sys
input = sys.stdin.readline

def solution(stickers, N):
    if N == 1:
        return max(stickers[0][0], stickers[1][0])
    
    # dp 테이블을 초기화
    dp = [[0] * N for _ in range(2)]
    
    # 초기값 설정
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    
    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]
    
    # 동적 프로그래밍 진행
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1] + stickers[0][i], dp[1][i-2] + stickers[0][i])
        dp[1][i] = max(dp[0][i-1] + stickers[1][i], dp[0][i-2] + stickers[1][i])
    
    return max(dp[0][N-1], dp[1][N-1])

# 입력 처리 및 실행
T = int(input())

for _ in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    
    # solution 호출 및 결과 출력
    result = solution(stickers, N)
    print(result)
