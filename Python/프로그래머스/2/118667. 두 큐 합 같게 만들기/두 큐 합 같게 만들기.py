def solution(queue1, queue2):
    n = len(queue1)
    total = sum(queue1)+sum(queue2)
    if total%2 != 0:
        return -1
    queue = queue1 + queue2
    
    left, right = 0, n
    left_sum = sum(queue1)
    answer = 0
    while left < right and right < 2*n :
        if left_sum == total//2 :
            return answer
        if left_sum > total//2 :
            left_sum -= queue[left]
            left+=1
        elif left_sum < total//2 :
            left_sum += queue[right]
            right+=1
        answer+=1
    
    return -1
            
                
    
        
    
    return answer