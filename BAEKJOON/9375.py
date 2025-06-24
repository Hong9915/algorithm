import sys
from collections import defaultdict
input = sys.stdin.readline

def outfit_cases(clothes):
    # 가능한 경우의 수를 계산합니다.
    result = 1
    for category in clothes.values():
        result *= (len(category) + 1)  
    return result - 1  

T = int(input().strip())

for _ in range(T):
    clothes = defaultdict(list)
    n = int(input().strip())
    for _ in range(n):
        a, b = map(str, input().strip().split())
        clothes[b].append(a)  
    print(outfit_cases(clothes))
