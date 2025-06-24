import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())

def conquer(A, B, C):
    if B == 1:
        return A % C

    if B % 2 == 0:
        temp = conquer(A, B // 2, C)
        return (temp * temp) % C
    else:
        temp = conquer(A, B // 2, C)
        return (temp * temp * A) % C

print(conquer(A, B, C))
