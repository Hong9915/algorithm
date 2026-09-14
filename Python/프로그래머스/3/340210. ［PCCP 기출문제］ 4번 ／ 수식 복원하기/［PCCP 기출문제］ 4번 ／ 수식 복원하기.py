def to_base(n, base):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result

def is_valid_number(s, base):
    """숫자 문자열이 해당 진법에서 유효한지 확인"""
    try:
        int(s, base)
        return True
    except ValueError:
        return False

def solution(expressions):
    possible_bases = set(range(2, 10))
    answer = []

    for exp in expressions:
        A, op, B, eq, C = exp.split()
        
        # X 포함 여부 관계없이 A, B의 숫자로 진법 좁히기
        for base in range(2, 10):
            if not is_valid_number(A, base) or not is_valid_number(B, base):
                possible_bases.discard(base)
        
        # C가 X가 아니면 등식으로도 좁히기
        if C != "X":
            for base in range(2, 10):
                if base not in possible_bases:
                    continue
                try:
                    a = int(A, base)
                    b = int(B, base)
                    c = int(C, base)
                    result = a + b if op == "+" else a - b
                    if result != c:
                        possible_bases.discard(base)
                except ValueError:
                    possible_bases.discard(base)

    for exp in expressions:
        A, op, B, eq, C = exp.split()
        if C != "X":
            continue

        results = set()
        for base in possible_bases:
            try:
                a = int(A, base)
                b = int(B, base)
                val = a + b if op == "+" else a - b
                results.add(to_base(val, base))
            except ValueError:
                continue

        X = results.pop() if len(results) == 1 else "?"
        answer.append(" ".join([A, op, B, eq, str(X)]))

    return answer