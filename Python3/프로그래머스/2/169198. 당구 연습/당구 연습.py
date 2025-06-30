def solution(m, n, startX, startY, balls):
    answer = []

    for ballX, ballY in balls:
        min_dist_sq = float('inf')  

        if not (startY == ballY and startX > ballX):  
            reflectX = -ballX
            reflectY = ballY
            dist_sq = (startX - reflectX) ** 2 + (startY - reflectY) ** 2
            min_dist_sq = min(min_dist_sq, dist_sq)

        if not (startY == ballY and startX < ballX):
            reflectX = 2 * m - ballX
            reflectY = ballY
            dist_sq = (startX - reflectX) ** 2 + (startY - reflectY) ** 2
            min_dist_sq = min(min_dist_sq, dist_sq)

        if not (startX == ballX and startY > ballY):
            reflectX = ballX
            reflectY = -ballY
            dist_sq = (startX - reflectX) ** 2 + (startY - reflectY) ** 2
            min_dist_sq = min(min_dist_sq, dist_sq)

        
        if not (startX == ballX and startY < ballY):
            reflectX = ballX
            reflectY = 2 * n - ballY
            dist_sq = (startX - reflectX) ** 2 + (startY - reflectY) ** 2
            min_dist_sq = min(min_dist_sq, dist_sq)

        answer.append(min_dist_sq)

    return answer
