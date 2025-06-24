ABC = 1
for _ in range(3):
    num = int(input())
    ABC *= num

num_str = str(ABC)

for i in range(10):
    print(num_str.count(str(i)))
