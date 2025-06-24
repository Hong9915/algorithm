import sys
input=sys.stdin.readline
N=int(input())

plane=[]

for _ in range(N):
    plane.append(list(map(int, input().strip().split())))


def quick_sort(lst):
    if len(lst)<=1:
        return lst
    
    pivot=lst[len(lst)//2][0]
    left=[x for x in lst if x[0] < pivot]
    middle=[x for x in lst if x[0] == pivot]
    if len(middle)>=2:
        middle.sort(key=lambda y: y[1])
    right=[x for x in lst if x[0] > pivot]
    
    return quick_sort(left)+ middle + quick_sort(right)

plane=quick_sort(plane)
for coords in plane:
    print(f"{coords[0]} {coords[1]}")