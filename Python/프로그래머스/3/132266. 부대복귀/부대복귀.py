from collections import defaultdict,deque


def solution(n, roads, sources, destination):
    dic = defaultdict(list)
    
    for st, en in roads :
        dic[st].append(en)
        dic[en].append(st)
    
    dist = [-1] * (n + 1)
    dist[destination] = 0
    q = deque([destination])

    while q:
        cur = q.popleft()
        for nxt in dic[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    return [dist[s] for s in sources]