import sys

input = sys.stdin.readline

def factorial(N):
    if N == 0 or N == 1:
        return 1
    return factorial(N-1) * N

N, M = map(int, input().strip().split())

cards = list(map(int, input().strip().split()))

results=[]
for i in range(len(cards)):
     for j in range(i+1,len(cards)):
         for z in range(j+1,len(cards)):
             if (cards[i]+cards[j]+cards[z]) > M:
                 continue
             else:
                results.append(cards[i]+cards[j]+cards[z])
print(max(results))