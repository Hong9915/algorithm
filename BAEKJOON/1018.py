def count_chess(matrix):
    count_W_start = 0
    count_B_start = 0
    
    # 체스판을 한 번 탐색하면서 체스판 색칠 개수를 센다
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if matrix[i][j] != 'W':
                    count_W_start += 1
                if matrix[i][j] != 'B':
                    count_B_start += 1
            else:
                if matrix[i][j] != 'W':
                    count_B_start += 1
                if matrix[i][j] != 'B':
                    count_W_start += 1
                    
    return min(count_W_start, count_B_start)
#두번 돌리지말고 한번에해야됨
def find_min_chess(matrix, M, N):
    results = []
    for i in range(M-7):
        for j in range(N-7):
            sub_matrix = [row[j:j+8] for row in matrix[i:i+8]]
            results.append(count_chess(sub_matrix))

    return min(results)
M, N = map(int, input().split())

matrix = []
for i in range(M):
    row = list(map(str, input()))  
    matrix.append(row) 



print(find_min_chess(matrix,M,N))
