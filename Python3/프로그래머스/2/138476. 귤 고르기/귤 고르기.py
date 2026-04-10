

def solution(k, tangerine):
    answer = 0
    count = {}
    for tanger in tangerine :
        count[tanger] = count.get(tanger,0)+1
        
    sorted_count=sorted(count.values(), reverse=True)
    tmp=0
    for value in sorted_count :
        tmp+=value
        answer+=1
        if tmp >= k :
            return answer
    
    return answer