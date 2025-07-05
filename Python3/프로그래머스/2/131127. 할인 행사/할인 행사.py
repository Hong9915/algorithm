from collections import Counter

def solution(want, number, discount):
    answer = 0
    target = dict(zip(want, number)) 

    for i in range(len(discount) - 9): 
        window = discount[i:i+10]
        window_count = Counter(window)
        if window_count == target:
            answer += 1

    return answer
