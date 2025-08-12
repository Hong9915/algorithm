import math

def to_base_k(n, k):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % k))
        n //= k
    return ''.join(reversed(digits))

def is_prime(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    base_k = to_base_k(n, k)
    # print(base_k)
    parts = [p for p in base_k.split('0') if p != '']
    count = 0
    # print(parts)
    for part in parts:
        val = int(part)
        # print(val)
        if is_prime(val):
            count += 1
    return count


