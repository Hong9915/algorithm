def solution(signals):
    answer = -1
    cycles = []
    y_start_end = []
    total_cycle = 1
    
    for signal in signals:
        cycles.append(sum(signal))
        y_start_end.append([signal[0], signal[0] + signal[1]])
        total_cycle *= sum(signal)
    
    for time in range(1, total_cycle):
        if all(y_start_end[i][0] <= time % cycles[i] < y_start_end[i][1]
               for i in range(len(signals))):
            answer = time + 1
            break
    
    return answer