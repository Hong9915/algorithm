import sys
input = sys.stdin.readline

def greedy_algorithm(N, coins):
    answer = 0
    
    for coin in reversed(coins):   
        if N >= coin:
            answer += N // coin   
            N %= coin             #
    
    return answer


N, K = map(int, input().strip().split())
coins = []
for _ in range(N):
    coins.append(int(input().strip()))

# 그리디 알고리즘 실행
result = greedy_algorithm(K, coins)
print(result)
