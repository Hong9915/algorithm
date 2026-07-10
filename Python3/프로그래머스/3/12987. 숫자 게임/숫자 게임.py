"""
A팀을 오름차순으로 정렬하고
A팀보다 1큰 가장 작은 숫자를 B에서 가져오면 가장 큰 승점?
"""

def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    com_len = len(A)
    done = [False] * len(B)
    start = 0
    
    for i in range(com_len):
        for j in range(start,com_len):
            if A[i] < B[j] and not done[j] :
                start = j + 1
                answer += 1
                done[j] = True
                if start == com_len:
                    return answer
                break
    
    
    return answer