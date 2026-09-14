def solution(targets):
    targets.sort(key=lambda x:x[1])
    
    answer = 0
    line = -float("inf")
    for s , e in targets:
        if line < s :
            line = e-0.1
            answer +=1
        
    return answer