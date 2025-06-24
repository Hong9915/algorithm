test_case = int(input())
results=[]
for i in range(test_case):
    R, S = input().split()
    R = int(R)
    result = ''
    for char in S:
        result += char * R
    results.append(result)

for result in results :
    print(result)
