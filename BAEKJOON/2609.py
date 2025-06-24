
def gcd(a, b):
    while b != 0:            # b가 0이 아닌 동안 반복
        a, b = b, a % b      # a에 b를, b에 a를 b로 나눈 나머지를 대입
    return a                 # b가 0이 되면 a를 반환 (최소공약수)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 두 수를 입력받기
a, b = map(int, input().split())

# GCD와 LCM 계산
gcd_value = gcd(a, b)
lcm_value = lcm(a, b)

print(gcd_value)
print(lcm_value)
