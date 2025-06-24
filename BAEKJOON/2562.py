max_value = 0
max_index = 0
num_list = []

for i in range(9):
    x = int(input())
    if x > max_value:
        max_value = x
        max_index = i
    num_list.append(x)

print(max_value)
print(max_index + 1)  # 1을 더해서 몇 번째 수인지를 출력
