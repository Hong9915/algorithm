from itertools import combinations

def solution(n, q, ans):
    answer = 0
    for secret in combinations(range(1, n+1), 5):
        valid = True
        for i in range(len(q)):
            nums = q[i]
            match = len(set(secret) & set(nums))
            if match != ans[i]:
                valid = False
                break
        if valid:
            answer += 1
    return answer
