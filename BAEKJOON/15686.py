import sys
input=sys.stdin.readline
from itertools import combinations

def calculate_chicken_distance(houses, chicken_stores):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in chicken_stores:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

def solution():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    
    houses = []
    chicken_stores = []
    
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chicken_stores.append((i, j))
    
    chicken_combinations = list(combinations(chicken_stores, M))
    
    min_chicken_distance = float('inf')
    for combination in chicken_combinations:
        city_distance = calculate_chicken_distance(houses, combination)
        min_chicken_distance = min(min_chicken_distance, city_distance)
    
    print(min_chicken_distance)

solution()
