import sys
input=sys.stdin.readline

def grade(lst):
    LEN=len(lst)
    result=[]
    for i in range(LEN):
        _grade=LEN
        for j in range(LEN):
            if i==j:
                continue
            if lst[i][0]>=lst[j][0] and lst[i][1]>=lst[j][1]:
                _grade-=1
            elif lst[i][0]>=lst[j][0] or lst[i][1]>=lst[j][1]:
                _grade-=1
        result.append(_grade)
    return result
N=int(input())
weight_height=[]
for _ in range(N):
    weight_height.append(list(map(int,input().strip().split())))

result_grade=grade(weight_height)

print(' '.join(map(str, result_grade)))