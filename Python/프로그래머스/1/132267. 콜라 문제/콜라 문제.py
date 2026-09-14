def solution(a, b, n):
    empty_bottles = n
    total_cola = 0
    while empty_bottles >= a:
        new_cola = empty_bottles // a *b
        total_cola += new_cola
        empty_bottles = (empty_bottles % a) + new_cola  
    return total_cola

