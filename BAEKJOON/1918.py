import sys

input = sys.stdin.readline

expression = input().strip() 


precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
stack = []  
output = []  

for token in expression:
    if token.isalnum():  
        output.append(token)
    elif token == "(": 
        stack.append(token)
    elif token == ")":  
        while stack and stack[-1] != "(":
            output.append(stack.pop())
        stack.pop()  # 여는 괄호 제거
    else:  # 연산자일 경우
        while stack and precedence[stack[-1]] >= precedence[token]:
            output.append(stack.pop())  # 높은 우선순위 연산자 먼저 출력
        stack.append(token)

# 남아있는 연산자 모두 출력
while stack:
    output.append(stack.pop())

print("".join(output))  # 후위 표기법 출력
