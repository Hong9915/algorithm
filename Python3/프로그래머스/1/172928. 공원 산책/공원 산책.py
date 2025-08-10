def solution(park, routes):
    H, W = len(park), len(park[0])
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                y, x = i, j
                break
    directions = {
        'E': (0, 1),
        'W': (0, -1),
        'S': (1, 0),
        'N': (-1, 0)
    }
    
    for route in routes:
        d, dist = route.split()
        dist = int(dist)
        dy, dx = directions[d]
        
        ny, nx = y, x
        blocked = False
        
        for _ in range(dist):
            ny += dy
            nx += dx
            if not (0 <= ny < H and 0 <= nx < W):
                blocked = True
                break
            if park[ny][nx] == 'X':
                blocked = True
                break
        
        if not blocked:
            y, x = ny, nx
    
    return [y, x]
