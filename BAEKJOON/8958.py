test_case = int(input())

for _ in range(test_case):
    OX_result=str(input())
    O_a=0
    count=0
    for i in range(len(OX_result)):
        if OX_result[i]=="O":
            O_a+=1
        elif OX_result[i]=="X":
            O_a=0
        count+=O_a
    print(count)