num_list = list(map(int,input().split()))
total = 0
for num in num_list:
    total += num*num
print(total%10)