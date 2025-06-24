import sys

input = sys.stdin.readline

fibona = 1_000_000_007
N = int(input().strip())

def fib_matrix(n):
    if n == 0:
        return 0  # F(0) = 0

    def multiply(A, B):
        return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % fibona,
                 (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % fibona],
                [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % fibona,
                 (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % fibona]]

    def power(A, n):
        res = [[1, 0], [0, 1]]
        while n:
            if n % 2:
                res = multiply(res, A)
            A = multiply(A, A)
            n //= 2
        return res

    base = [[1, 1], [1, 0]]
    return power(base, n - 1)[0][0]

print(fib_matrix(N))
