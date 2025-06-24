import sys
input=sys.stdin.readline
r=31
M=1234567891

L=int(input().strip())
string=input().strip()

answer=0

for i in range(L):
    answer+=(ord(string[i])-96)*(31**i)

print(answer%M)
