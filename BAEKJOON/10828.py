# class STACK:
#     def __init__(self):
#         self.result=[]
    
#     def push(self, X):
#         self.result.append(X)
        
#     def pop(self):
#         if self.result:
#             return self.result.pop()
#         else:
#             return -1
    
#     def size(self):
#         return len(self.result)
    
#     def empty(self):
#         if self.result:
#             return 0
#         else:
#             return 1
#     def top(self):
#         if self.result:
#             return self.result[-1]
        
#         else:
#             return -1
        
# N=(int(input()))

# temp_stack=STACK()
# for _ in range(N):
#     operation=str(input().split())
    
#     if "push" in operation:
#         num=""
#         for char in operation:
#         # 문자가 숫자인지 확인
#             if char.isdigit():
#             # 숫자라면 결과 문자열에 추가
#                 num += char
#         temp_stack.push(int(num))
#     elif "pop" in operation:
#         print(temp_stack.pop())
#     elif "size" in operation:
#         print(temp_stack.size())
#     elif "empty" in operation:
#         print(temp_stack.empty())
#     elif "top" in operation:
#         print(temp_stack.top())


#gpt 코드
class STACK:
    def __init__(self):
        self.result = []
    
    def push(self, X):
        self.result.append(X)
        
    def pop(self):
        if self.result:
            return self.result.pop()
        else:
            return -1
    
    def size(self):
        return len(self.result)
    
    def empty(self):
        return 0 if self.result else 1
    
    def top(self):
        if self.result:
            return self.result[-1]
        else:
            return -1

# 첫째 줄에 명령의 수 N을 입력받습니다.
N = int(input().strip())

# 스택 인스턴스를 생성합니다.
temp_stack = STACK()

# 결과를 저장할 리스트를 만듭니다.
output = []

# 명령어를 처리합니다.
for _ in range(N):
    command = input().strip()
    if command.startswith("push"):
        _, num = command.split()
        temp_stack.push(int(num))
    elif command == "pop":
        output.append(temp_stack.pop())
    elif command == "size":
        output.append(temp_stack.size())
    elif command == "empty":
        output.append(temp_stack.empty())
    elif command == "top":
        output.append(temp_stack.top())

# 결과를 출력합니다.
print("\n".join(map(str, output)))

