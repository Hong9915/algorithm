N = int(input())

if N == 1:
    print(1)
else:
    _sum = 1
    count = 1
    while _sum < N:
        _sum += 6 * count
        count += 1
    print(count)
