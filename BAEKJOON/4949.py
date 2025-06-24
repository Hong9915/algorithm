def check_balance(sentence):
    stack = []  # 괄호를 저장할 스택
    
    for char in sentence:
        if char in "([":  # 여는 괄호는 스택에 추가
            stack.append(char)
        elif char == ")":  # 닫는 소괄호
            if not stack or stack[-1] != "(":  # 스택이 비어있거나 마지막이 여는 소괄호가 아니면 불균형
                return "no"
            stack.pop()  # 짝을 맞추었으므로 스택에서 제거
        elif char == "]":  # 닫는 대괄호
            if not stack or stack[-1] != "[":  # 스택이 비어있거나 마지막이 여는 대괄호가 아니면 불균형
                return "no"
            stack.pop()  # 짝을 맞추었으므로 스택에서 제거
    if stack:  # 모든 과정을 마친 후에도 스택에 남아있으면 불균형
        return "no"
    
    return "yes"  # 모든 괄호가 균형을 이루면

while True:
    sentence = input()
    if sentence == ".":  # 종료 조건
        break
    print(check_balance(sentence))
