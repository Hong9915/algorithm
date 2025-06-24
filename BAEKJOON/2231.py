N = int(input())

def find_N(N):
    for num in range(1, N + 1):
        result_sum = num + sum(map(int, str(num)))#각 자리수의 합
        if result_sum == N:
            return num
    return 0

print(find_N(N))
