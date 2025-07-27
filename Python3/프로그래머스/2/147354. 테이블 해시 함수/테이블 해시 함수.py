def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    result = 0

    for i in range(row_begin - 1, row_end):
        row = data[i]
        S_i = sum([val % (i + 1) for val in row])
        result ^= S_i

    return result
