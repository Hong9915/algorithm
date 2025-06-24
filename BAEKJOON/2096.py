import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    

    min_prev = list(map(int, input().strip().split()))
    max_prev = min_prev[:]  
    for _ in range(1, N):
        row = list(map(int, input().strip().split()))
        min_curr = [0] * 3
        max_curr = [0] * 3
 
        min_curr[0] = row[0] + min(min_prev[0], min_prev[1])
        max_curr[0] = row[0] + max(max_prev[0], max_prev[1])

        min_curr[1] = row[1] + min(min_prev[0], min_prev[1], min_prev[2])
        max_curr[1] = row[1] + max(max_prev[0], max_prev[1], max_prev[2])

        min_curr[2] = row[2] + min(min_prev[1], min_prev[2])
        max_curr[2] = row[2] + max(max_prev[1], max_prev[2])

        min_prev = min_curr
        max_prev = max_curr

    return max(max_prev), min(min_prev)

max_val, min_val = solution()
print(max_val, min_val)
