from collections import defaultdict

def solution(points, routes):
    visited = defaultdict(int) 
    collision=0
    for route in routes :
        time=0
        cur_y,cur_x=points[route[0]-1]
        visited[(0, (cur_y, cur_x))] += 1 

        for i in range(1, len(route)):
            tar_y, tar_x = points[route[i] - 1]

            while cur_y != tar_y:
                cur_y += 1 if cur_y < tar_y else -1
                time += 1
                visited[(time, (cur_y, cur_x))] += 1

            while cur_x != tar_x:
                cur_x += 1 if cur_x < tar_x else -1
                time += 1
                visited[(time, (cur_y, cur_x))] += 1

        
    for count in visited.values() :
        if count > 1:
            collision+=1
        

    answer = collision
    
    return answer