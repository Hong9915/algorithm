def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        max_y = int((d ** 2 - x ** 2) ** 0.5)  
        count_y = max_y // k + 1            
        answer += count_y
    return answer
