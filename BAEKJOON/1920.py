N=int(input())

A=list(map(int, input().split()))
A=sorted(A)

M=int(input())

B=list(map(int, input().split()))

def binary_search(num,sorted_list):
    left, right = 0 , len(sorted_list) -1
    
    while(right>=left):
        mid = (left+right)//2
        if num > sorted_list[mid]:
            left = mid+1
        elif num < sorted_list[mid]:
            right = mid-1
        elif num == sorted_list[mid]:
            return 1
        
    return 0

for num in B:
    print(binary_search(num,A))

            