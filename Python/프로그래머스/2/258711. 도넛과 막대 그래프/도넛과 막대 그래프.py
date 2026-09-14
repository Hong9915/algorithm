from collections import defaultdict

def solution(edges):
    
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    
    nodes = set()
    
    for u,v in edges :
        out_deg[u] += 1
        in_deg[v] += 1
        nodes.add(u)
        nodes.add(v)
    
    root = -1
    for node in nodes :
        if in_deg.get(node, 0) == 0  and out_deg[node] >= 2:
            root = node
            break
    
    for u,v in edges :
        if u == root :
            in_deg[v] -= 1
    
    eight_count = 0
    for node in nodes :
        if node != root and in_deg[node] == 2 and out_deg[node] == 2:
            eight_count +=1
    
    bar_count = 0
    
    for node in nodes :
        if node != root and out_deg[node]==0:
            bar_count+=1
    
    donut_count= out_deg[root] - bar_count - eight_count
    
    answer = [root, donut_count,bar_count,eight_count]
    return answer