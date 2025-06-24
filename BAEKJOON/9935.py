import sys

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
result = []

for c in string:
    result.append(c) 

    if len(result) >= len(bomb) and ''.join(result[-len(bomb):]) == bomb:
        # 폭발 문자열이 발견되면 제거
        for _ in range(len(bomb)):
            result.pop()

# 결과 출력
if result:
    print(''.join(result))  # 스택의 모든 문자를 합쳐 출력
else:
    print("FRULA")  # 스택이 비어 있으면 "FRULA"
