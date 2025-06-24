import sys
input = sys.stdin.readline

def find_xy(M, N, x, y):
    # x를 기준으로 하는 모든 해 k = x + i * M
    k = x
    
    # k % N이 y와 같을 때, 해를 찾음.
    while k <= M * N:
        if (k - y) % N  == 0:
            return k
        k += M
    
    # 찾을 수 없는 경우 -1 반환
    return -1

T = int(input().strip())

for _ in range(T):
    M, N, x, y = map(int, input().strip().split())
    print(find_xy(M, N, x, y))
