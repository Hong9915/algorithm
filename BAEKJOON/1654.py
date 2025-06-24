N,K=map(int,input().split())
LAN_line=[]
for _ in range(N):
    LAN_line.append(int(input()))

#binary search는 시간 복잡도가 O(log N)
def count_result(result, LAN_line):
    count=0
    for LAN in LAN_line:
        count+=LAN//result
    return count
def binary_search_length(K,N,LAN_line):
    left, right = 1, max(LAN_line) # 왼쪽은 가장 작은 값 #오른쪽은 될 수 있는 가장 큰 값
    result=0
    
    while left <= right: 
        mid= (left+right)//2
        if count_result(mid,LAN_line) >= K:
            result=mid
            left=mid+1
        else:
            right= mid-1
        
    return result
    
print(binary_search_length(K,N,LAN_line))

