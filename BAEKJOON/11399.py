import sys

input=sys.stdin.readline

N=int(input())

array=list(map(int,input().strip().split()))
    
array.sort()

def program(array):
    result=0
    time=0
    for money in array:
        time+=money
        result+=time
    return result

print(program(array))