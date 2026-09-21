def solution(sequence):
    answer = 0

    for pattern in [1, -1]:
        current = 0

        for i, value in enumerate(sequence):
            value *= pattern * (-1) ** i

            current = max(value, current + value)
            answer = max(answer, current)

    return answer