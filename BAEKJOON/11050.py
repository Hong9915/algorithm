import sys
input=sys.stdin.readline
def factorial(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result
        

def binomial_coefficient(N,K):
    if N==K:
        return 1
    
    return factorial(N)//(factorial(N-K)*factorial(K))

N,K=map(int,input().strip().split())

print(binomial_coefficient(N,K))