def solution(picks, minerals):
    fatigue = {
        "diamond": [1, 5, 25],  # 다이아 곡괭이, 철 곡괭이, 돌 곡괭이 피로도 순
        "iron":    [1, 1, 5],
        "stone":   [1, 1, 1]
    }

    max_chunks = sum(picks)
    chunks = []
    for i in range(0, len(minerals), 5):
        if max_chunks == 0:
            break
        chunk = minerals[i:i+5]
        chunks.append(chunk)
        max_chunks -= 1

    def calc_fatigue(chunk):
        return sum(fatigue[m][2] for m in chunk)

    chunks.sort(key=calc_fatigue, reverse=True)


    pick_order = []
    for i, cnt in enumerate(picks):
        pick_order += [i] * cnt  
    print(pick_order)
    answer = 0
    for i in range(len(chunks)):
        if i >= len(pick_order):
            break  
        pick = pick_order[i]
        for mineral in chunks[i]:
            answer += fatigue[mineral][pick]

    return answer
