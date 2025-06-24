# 시간초과 실패
# N=int(input())

# numbers=[]
# for _ in range(N):
#     numbers.append(int(input()))

# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     mid = len(lst) // 2
#     pivot = lst[mid]
#     left = [x for x in lst if x < pivot]
#     middle = [x for x in lst if x == pivot]
#     right = [x for x in lst if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)


# for num in quick_sort(numbers):
#     print(num)

import sys
input = sys.stdin.readline
N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))


for num in sorted(numbers):
    print(num)

# 가장 빠른코드
# def sol():
#     a=[None]*2000001
#     b=map(int,open(0))
#     next(b)
#     for i in b:a[i]=1
#     print("\n".join(str(i) for i in range(-1000000,1000001,1) if a[i]))

# sol()
