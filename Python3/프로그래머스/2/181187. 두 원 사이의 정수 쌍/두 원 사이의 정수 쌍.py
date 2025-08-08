import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1): 
        maxY = math.floor((r2**2 - x**2)**0.5)
        minY = math.ceil((r1**2 - x**2)**0.5) if x < r1 else 0
        answer += (maxY - minY + 1)  
    return answer * 4 