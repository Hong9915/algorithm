from collections import deque
import sys

def hide_and_seek(N, K):
    if N >= K: 
        return N - K

    max_limit = 100000
    dp = [-1] * (max_limit + 1) 
    queue = deque([N])
    dp[N] = 0

    while queue:
        current = queue.popleft()

        if current == K:
            return dp[current]
        if 0 <= current*2 <= max_limit and dp[current*2] == -1:
            dp[current*2]=dp[current]
            queue.append(current*2)
        for next_pos in (current - 1, current + 1):
            if 0 <= next_pos <= max_limit and dp[next_pos] == -1:
                dp[next_pos] = dp[current] + 1
                queue.append(next_pos)
        

input = sys.stdin.readline
N, K = map(int, input().strip().split())

print(hide_and_seek(N, K))
