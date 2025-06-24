N,K= map(int,input().split())
modulus = 1000000007
def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % modulus
    return n

# 거듭제곱 계산(나머지 연산 적용)
def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
     
    tmp = square(n, k//2)
    if k % 2: # 홀수일때
        return tmp * tmp * n % modulus
    else: #짝수일때
        return tmp * tmp % modulus

# result = calculate_modulo_binomial_coefficient(N, K, modulus)
# result = pow(int(factorial(N)/(factorial(N-K)*factorial(K))), -modulus+2, modulus)
# print(result)
top = factorial(N)
bot = factorial(N-K) * factorial(K) % modulus

# 페르마의 소정리 이용해서 조합 공식 곱셈 형태로 변형
print(top * square(bot, modulus-2) % modulus)
