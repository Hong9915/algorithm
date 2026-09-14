def solution(numLog):
    answer = []
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i - 1]
        if diff == 1:
            answer.append("w")
        elif diff == -1:
            answer.append("s")
        elif diff == 10:
            answer.append("d")
        elif diff == -10:
            answer.append("a")
    return "".join(answer)