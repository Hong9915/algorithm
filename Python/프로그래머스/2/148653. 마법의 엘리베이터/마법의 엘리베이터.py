def solution(storey):
    answer = 0
    while storey > 0:
        digit = storey % 10
        if digit > 5:
            answer += 10 - digit
            storey += 10 
        elif digit < 5:
            answer += digit
        else:  
            if (storey // 10) % 10 >= 5:
                answer += 5
                storey += 10 
            else:
                answer += 5
        storey //= 10
    return answer
