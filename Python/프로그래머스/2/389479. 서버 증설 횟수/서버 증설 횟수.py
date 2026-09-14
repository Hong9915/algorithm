from collections import deque

def solution(players, m, k):
    answer = 0
    active = deque()  

    for t in range(24):
        while active and active[0] <= t:
            active.popleft()
        print(active)
        need = players[t] // m
        # if players[t] % m > 0:
        #     need += 1

        running = len(active)

        if running < need:
            add = need - running
            for _ in range(add):
                active.append(t + k)
            answer += add
            print(f"{t} ~ {t+1}시: {add}번")

    print(f"총 {answer}번 서버를 증설해야 합니다.")
    return answer
