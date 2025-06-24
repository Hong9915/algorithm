# 주기의 길이가 P 이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같습니다.
# M = 10k 일 때, k > 2 라면, 주기는 항상 15 × 10k-1 입니다. 이 사실을 모른다고 해도, 주기를 구하는 코드를 이용해서 문제를 풀 수 있습니다.
mod = 1000000
p = mod //10 *15
fibo = [0, 1]

if __name__ == "__main__":
    num = int(input())
    for i in range(2, p):
        fibo.append(fibo[i - 1] + fibo[i - 2])
        fibo[i] %= mod
    print(fibo[num % p])
