M , N = map(int, input().split())
def prime_num(X):
    if X < 2:
        return False
    for i in range (2, int(X**0.5)+1,1):
        if (X%i==0):
            return False
    return True

results=[]
for num in range (M, N+1):
    if prime_num(num):
        results.append(str(num))
    
print("\n".join(results))