from collections import Counter

def solution(weights):
    counter = Counter(sorted(weights))
    answer = 0

    for weight in counter:
        n = counter[weight]
        answer += n * (n - 1) // 2
    
    ratios = [2/3, 2/4, 3/4]
    
    for weight in counter :
        for ratio in ratios:
            if (weight/ratio) in counter :
                answer+=counter[weight]*counter[weight/ratio]
    
    return answer