#   
def solution(n, times):
    left = 1
    right = max(times) * n
    
    while left < right :
        mid = (left+right)//2
        person = 0
        for time in times:
            person += mid//time
        if person >= n :
            right = mid
        elif person < n :
            left = mid +1



            
    answer = left
    return answer