import sys

MOD=1_000_000_007
def mod_inv(b, mod):
    return pow(b, mod - 2, mod)

def main():
    M = int(sys.stdin.readline().strip())
    a, b = 0, 1
    
    for _ in range(M):
        Ni, Si = map(int, sys.stdin.readline().split())
        a = (a * Ni + Si * b) % MOD
        b = (b * Ni) % MOD
    
    b_inv = mod_inv(b, MOD)
    result = (a * b_inv) % MOD
    print(result)

if __name__ == "__main__":
    main()
