import re

def solution(s: str):
    groups = re.findall(r'\{([0-9,]+)\}', s)

    sets = [list(map(int, g.split(','))) for g in groups]

    sets.sort(key=len)

    seen = set()
    ans = []
    for arr in sets:
        for x in arr:
            if x not in seen:
                seen.add(x)
                ans.append(x)
                break
    return ans
