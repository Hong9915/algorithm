import math

def solution(n, w, num):
    num_row = (num - 1) // w 
    total_rows = math.ceil(n / w)  
    direction = 0  

    if total_rows % 2 == 0:  
        total_index = w - (n % w)
        if n % w == 0:
            total_index = 0
        direction = 1
    else:  
        total_index = (n % w) - 1
        if n % w == 0:
            total_index = w - 1
        direction = 0


    if num_row == total_rows - 1:
        return 1


    if num_row % 2 == 0: # 왼→오
        target_index = (num - 1) % w
    else: # 오→왼
        target_index = w - 1 - ((num - 1) % w)


    if direction == 0: # 마지막층 왼→오
        if target_index <= total_index:
            return (total_rows - num_row - 1) + 1
        else:
            return (total_rows - num_row - 2) + 1
    else:  # 마지막층 오→왼
        if target_index >= total_index:
            return (total_rows - num_row - 1) + 1
        else:
            return (total_rows - num_row - 2) + 1
