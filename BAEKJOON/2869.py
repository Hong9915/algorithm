import sys
input=sys.stdin.readline
A, B, V = map(int, input().strip().split())

def count_days(A,B,V):
    for i in range((V-A)//(A-B),V//(A-B)+1,1):
        if (i*(A-B)+A) >= V:
            return i +1
print(count_days(A,B,V))
    