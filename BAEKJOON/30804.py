import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
fruits = list(map(int, input().strip().split()))

fruit_count = defaultdict(int)

left = 0
max_length = 0

for right in range(N):
    fruit_count[fruits[right]] += 1
    while len(fruit_count) > 2:
        print(fruit_count)
        fruit_count[fruits[left]] -= 1
        if fruit_count[fruits[left]] == 0:
            del fruit_count[fruits[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)
