import sys
input = sys.stdin.readline

def FizzBuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"  # "buzz" -> "Buzz"
    else:
        return num

string = []
i = -1  # -1로 초기화하여 숫자를 찾지 못한 경우의 예외 처리

for j in range(3):
    temp = input().strip()
    string.append(temp)
    try:
        num = float(temp)
        if num.is_integer():  # 정수만 처리
            i = j
    except ValueError:
        pass

# i가 -1인 경우 숫자를 찾지 못한 경우 처리
if i == -1:
    print("No valid number found.")
else:
    # 리스트의 i번째 요소를 정수로 변환하고 연산 수행
    number = int(float(string[i])) + 3 - i
    print(FizzBuzz(number))
