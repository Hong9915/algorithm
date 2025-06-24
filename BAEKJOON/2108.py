def find_mode(lst):
    count_dict={}
    for item in lst:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item]=1
    max_count=0
    max_count_value=[]
    for key,value in count_dict.items():
        if value > max_count:
            max_count=value
    for key,value in count_dict.items():
        if value == max_count:
            max_count_value.append(key)
            
    sorted_max_count_value=sorted(max_count_value)
    return sorted_max_count_value[1]
        
N=int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(input()))
    
sorted_numbers=sorted(numbers)
print(sum(numbers)//len(numbers))
print(sorted_numbers[len(numbers)//2])
print(find_mode(numbers))
print(max(numbers)-min(numbers))

# 정답코드
# import sys

# input = sys.stdin.readline

# n = int(input())
# data = []

# _sum = 0
# count = dict()
# for _ in range(n):
#     x = int(input())
#     data.append(x)

#     _sum += x

#     if x not in count:
#         count[x] = 1
#     else:
#         count[x] += 1

# data.sort()

# # 산술평균
# print(round(_sum/n))

# # 중앙값
# print(data[n//2])

# # 최빈값
# freq = max(count.values())
# numbers = []
# for key, value in count.items():
#     if value == freq:
#         numbers.append(key)

# if len(numbers) == 1:
#     print(numbers[0])
# else:
#     print(sorted(numbers)[1])

# # 범위
# print(data[-1] - data[0])
