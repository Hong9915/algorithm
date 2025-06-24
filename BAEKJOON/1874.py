
result=[]

N=int(input())
num_list=[x+1 for x in range(N)]
result_end=[]

def find_num(num_list, number):
    i=0

    while(1): 
        if len(result)!=0 and result[-1] == number:
            result.pop(-1)
            result_end.append("-")
            return
        else:
            if len(num_list)==0:
                print("NO")
                exit()
            result.append(num_list.pop(0))
            result_end.append("+")
        i+=1
            

for _ in range(N):
    num=int(input())
    find_num(num_list,num)


for x in result_end:
    print(x)
    
    
    
# GPT코드
# N = int(input())
# sequence = [int(input()) for _ in range(N)]

# stack = []
# result = []
# current = 1

# for num in sequence: #받아온 값이
#     while current <= num: #현재 넣을 값이 받아온 값보다 작을때까지 push
#         stack.append(current)
#         result.append('+')
#         current += 1
    
#     if stack[-1] == num: #만약 내가 찾는 값이 같다면 pop
#         stack.pop()
#         result.append('-')
#     else: #아무것도 없었다면 
#         print("NO")
#         exit()

# print("\n".join(result)) #list를 출력하는 방식
