import sys
from collections import deque
input=sys.stdin.readline




def count_kevin_bacon(main_line, start, N):
    distances = [-1] * (N + 1)
    distances[start]=0
    queue=deque([start])
    
    while queue:
        current=queue.popleft()
        for neighbor in  main_line[current]:
            if distances[neighbor]==-1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return sum(distances[1:])
            
main_line={}
N,M=map(int,input().strip().split())
for _ in range(M):
    key, value = map(int, input().strip().split())
    if key in main_line:
        main_line[key].append(value)
    else:
        main_line[key] = [value]

    if value in main_line:
        main_line[value].append(key)
    else:
        main_line[value] = [key]
for key in main_line:
    main_line[key].sort()
    
result = []
for i in range(1, N + 1):
    x = count_kevin_bacon(main_line, i, N)
    result.append(x)
# 최솟값을 가진 인덱스를 찾습니다.
min_value = min(result)
min_index = result.index(min_value) + 1  # 1부터 시작하는 인덱스라면 +1


print(min_index)