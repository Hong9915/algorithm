def solution(sequence, k):
    x = len(sequence)
    left = 0
    right = 0
    total = sequence[left]
    min_len=float('inf')
    answer = []
    result=[]
    while right < x :
        if total == k :
            if min_len > (right-left+1):
                min_len = right-left+1
                result=[left,right]
            total-=sequence[left]
            left+=1

        elif total < k :
            right +=1
            if right < x :
                total +=sequence[right]
        else : 
            total-=sequence[left]
            left+=1
            
    answer=result

    
    return answer