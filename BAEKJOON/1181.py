def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if len(x)<len(pivot)]
    middle = [x for x in arr if len(x)==len(pivot)]
    right = [x for x in arr if len(x)>len(pivot)]
    middle=list(set(middle))
    middle=sorted(middle)
    
    return quicksort(left) + middle + quicksort(right)


N=int(input())

words = []
for _ in range(N):
    words.append(input())


sorted_words=quicksort(words)

for sorted_word in sorted_words:
    print(sorted_word)
    