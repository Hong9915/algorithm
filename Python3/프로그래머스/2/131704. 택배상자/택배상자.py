from collections import deque
def solution(order):
    n = len(order)
    queue = deque(range(1,n+1))
    
    sub = []
    answer = 0
    idx = 0
    while queue or sub :
        if queue and queue[0] == order[idx] :
            no = queue.popleft()
            idx+=1
            answer+=1
        elif queue :
            sub.append(queue.popleft())
            
        if sub and sub[-1] == order[idx]  :
            ns = sub.pop()
            idx+=1
            answer+=1
            continue


        
        if not queue and sub :
            return answer

        
    
    return answer