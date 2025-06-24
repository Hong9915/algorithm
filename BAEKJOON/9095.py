import sys
input = sys.stdin.readline

# 메모이제이션을 위한 리스트 초기화
a = [0] * 11
a[1] = 1
a[2] = 2
a[3] = 4

# 동적 프로그래밍을 사용하여 a 배열의 값을 계산
for i in range(4, 11):
    a[i] = a[i-1] + a[i-2] + a[i-3]

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    print(a[n])
