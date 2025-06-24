import sys
input = sys.stdin.readline

def change_poketmon(name_or_num, book, reverse_book):
    if name_or_num.isdigit():
        return book[int(name_or_num)]
    else:
        return reverse_book[name_or_num]

N, M = map(int, input().strip().split())
poketmon_book = {}
reverse_poketmon_book = {}

for i in range(1, N + 1):
    poketmon = input().strip()
    poketmon_book[i] = poketmon
    reverse_poketmon_book[poketmon] = i

for _ in range(M):
    query = input().strip()
    print(change_poketmon(query, poketmon_book, reverse_poketmon_book))
