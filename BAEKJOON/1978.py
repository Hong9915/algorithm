N=int(input())
TEST = list(map(int, input().split()))
def prime_num(X):
    if X < 2:
        return False
    for i in range (2, int(X**0.5)+1,1):
        if (X%i==0):
            return False
    return True

count=0
for i in range (N):
    if prime_num(TEST[i]):
        count+=1
print(count)
    
