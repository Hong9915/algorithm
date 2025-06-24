#다시
import sys
input = sys.stdin.readline

expression = input().strip().split("-")
result = []
_sum = 0

# 첫 번째 요소는 더하기
first_part = sum(map(int, expression[0].split("+")))
_sum += first_part

# 나머지 요소는 빼기
for num in expression[1:]:
    if "+" in num:
        num = sum(map(int, num.split("+")))
    else:
        num = int(num)
    _sum -= num

print(_sum)
