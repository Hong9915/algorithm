def solution(diffs, times, limit):
    def is_possible(level):
        time = times[0]
        for i in range(1, len(diffs)):
            if level >= diffs[i]:
                time += times[i]
            else:
                time += ((times[i] + times[i - 1]) * (diffs[i] - level)) + times[i]
        return time <= limit

    left, right = 1, max(diffs)
    answer = max(diffs)
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid -1
        else:
            left = mid + 1

    return answer
