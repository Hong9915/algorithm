import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    
    # 입력 문자열을 파싱하여 리스트로 변환
    number_str = input().strip()[1:-1]  # 양끝의 대괄호 제거
    if number_str:
        number_list = deque(map(int, number_str.split(',')))  # deque 사용
    else:
        number_list = deque()

    reversed_flag = False  # 리스트가 뒤집힌 상태인지 추적
    error_flag = False

    for cmd in p:
        if cmd == "R":
            reversed_flag = not reversed_flag  # 뒤집힌 상태 변경
        elif cmd == "D":
            if number_list:
                if reversed_flag:
                    number_list.pop()  # 뒤집힌 상태면 마지막 요소 제거
                else:
                    number_list.popleft()  # 그렇지 않으면 첫 번째 요소 제거
            else:
                print("error")
                error_flag = True
                break

    if not error_flag:
        if reversed_flag:
            number_list.reverse()  # 최종적으로 뒤집힌 상태이면 리스트를 뒤집음
        print("[" + ",".join(map(str, number_list)) + "]")
