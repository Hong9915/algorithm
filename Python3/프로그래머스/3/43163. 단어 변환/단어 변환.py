"""
begin 부터해서 하나차이나는거를 재귀해서 들어가서 최종적으로 도달하면 스탑 후 return
"""

from collections import deque

def check_difference(c_word, word):

    difference = 0
    for i in range(len(c_word)):
        if difference > 1:
            return False
        if c_word[i] != word[i]:
            difference += 1
    if difference == 1:
        return True
def solution(begin, target, words):
    visited = [False] * len(words)
    
    if target not in words: # 만약 안에 없으면 바로 리턴
        return 0
    
    queue = deque([[begin,0]])
    
    while queue:
        c_word, step = queue.popleft()
        
        if c_word == target:
            return step
        
        for i, word in enumerate(words):
            if not visited[i] and check_difference(c_word,word):
                visited[i] = True
                queue.append([word,step+1])
            
        
        
    
    
    
    return 0