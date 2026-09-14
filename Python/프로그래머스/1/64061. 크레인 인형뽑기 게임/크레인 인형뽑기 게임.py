def solution(board, moves):
    answer = 0
    result = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] == 0:
                continue
            else:
                if result and result[-1]==board[i][move-1]:
                    answer+=2
                    result.pop(-1)
                else:
                    result.append(board[i][move-1])
                board[i][move-1] = 0
                break
    return answer