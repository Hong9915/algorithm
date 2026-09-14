def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)
    
    def dfs(cur_fat, count):
        nonlocal answer  
        answer = max(count, answer)
        
        for i in range(len(dungeons)):
            min_req_fat, con_fat = dungeons[i]
            if min_req_fat <= cur_fat and not visited[i]:
                visited[i] = True
                dfs(cur_fat - con_fat, count + 1)
                visited[i] = False
    
    dfs(k, 0)
    return answer