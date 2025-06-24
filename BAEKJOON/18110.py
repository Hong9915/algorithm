import sys
input=sys.stdin.readline


def my_round(num):
    if (num-int(num))>=0.5:
        return int(num)+1
    else:
        return int(num)
N=int(input().strip())
if(N==0):
    print(0)
    exit()
score=[]
for _ in range(N):
    score.append(int(input()))
    
score.sort()
x=my_round(N*0.15) # round는 반올림

if x>0:
    score=score[x:-x]


if (score):
    print(my_round(sum(score)/len(score)))
else:
    print(0)
