import math
N=int(input())

# def factorial(N):
#     if N==1 :
#         return 1
#     return factorial(N-1)*N

def count_zero(num):
    num_str=str(num)
    count=0
    for i in range (len(num_str)):
        if num_str[len(num_str)-i-1]!='0':
            break
        else:
            count+=1
    return count

print(count_zero(math.factorial(N)))