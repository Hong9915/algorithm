from collections import defaultdict, deque
"""
다익스트라 문제
visited 는 무한대로잡고
1번부터 탐색 그 다음에 연결되어있는 노드 탐색 
"""

def solution(n, edge):
    visited = [False]*(n+1)
    dic = defaultdict(list)
    
    
    for st, en in edge: # 양방향 연결
        dic[st].append(en)
        dic[en].append(st)
    
    queue = deque([1])
    visited[1] = True
    while queue :
        node = queue.popleft()

        for i in range(len(dic[node])): # 각 연결된 노드 돌기
            if not visited[dic[node][i]]:
                nx_node = dic[node][i] 
                visited[nx_node] = visited[node] + 1
                queue.append(nx_node)


    print(visited)
    return visited.count(max(visited))