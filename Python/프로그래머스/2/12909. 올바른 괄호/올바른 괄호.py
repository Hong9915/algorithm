from collections import deque

def solution(s):
    answer = True
    count_1 = 0
    count_2 = 0
    for x in s:
        if x == "(":
            count_1+=1
        elif x == ")":
            count_2+=1
            if count_1 < count_2:
                return False
    if count_1 != count_2:
            return False
    return True