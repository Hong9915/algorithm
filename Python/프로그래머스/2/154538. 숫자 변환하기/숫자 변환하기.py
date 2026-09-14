from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque([(x, 0)])  

    while queue:
        current, count = queue.popleft()

        if current == y:
            return count

        for next_num in (current + n, current * 2, current * 3):
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, count + 1))

    return -1  
