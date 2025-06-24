import sys

N, B = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def matrix_multiplication(matrix1, matrix2):
    temp_matrix = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            s = 0
            for i in range(N):
                s += matrix1[x][i] * matrix2[i][y]
                s %= 1000
            temp_matrix[x][y] = s   # 바로 나머지 연산 적용
    return temp_matrix


def division_conquer(matrix, num):
    if num == 1:
        return matrix
    half = division_conquer(matrix, num // 2)
    if num % 2 :
        return matrix_multiplication(matrix_multiplication(half, half),matrix)
    else:
        return matrix_multiplication(half,half)  # 바로 나머지 연산 적용


result = division_conquer(A, B)
for row in result:
    print(*[r%1000 for r in row])

