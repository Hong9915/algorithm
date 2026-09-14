def solution(routes):
    routes=sorted(routes,key = lambda route : route[1])
    answer = 1
    
    line = routes[0][1]
    for start, end in routes:
        if start <= line <= end:
            continue
        else:
            line = end
            answer +=1
    
    return answer