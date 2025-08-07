def solution(board):
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)
    o_win = False
    
    for i in range(3):
        row_count = 0
        column_count = 0 
        
        for j in range(3):
            if board[i][j] == "O":
                row_count += 1
            if board[j][i] == "O":
                column_count += 1  
                
        if row_count == 3 or column_count == 3:
            o_win = True
    
    if all(board[i][i] == "O" for i in range(3)):
        o_win = True
    if all(board[i][2 - i] == "O" for i in range(3)):
        o_win = True
    
    x_win = False
    
    for i in range(3):
        row_count = 0
        column_count = 0
        
        for j in range(3):
            if board[i][j] == "X":
                row_count += 1
            if board[j][i] == "X":
                column_count += 1
                
        if row_count == 3 or column_count == 3:
            x_win = True
    
    if all(board[i][i] == "X" for i in range(3)):
        x_win = True
    if all(board[i][2 - i] == "X" for i in range(3)):
        x_win = True
    if x_count > o_count:
        return 0  
    if o_count - x_count > 1:
        return 0  
    if o_win and x_win:
        return 0  
    if o_win and o_count != x_count + 1:
        return 0  
    if x_win and o_count != x_count:
        return 0  
    return 1