import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
table = [x for x in range(1, N + 1)]
result = []
index = 0

while table:
    index = (index + K - 1) % len(table)
    result.append(table.pop(index))
print("<",", ".join(map(str,result)),">",sep="")