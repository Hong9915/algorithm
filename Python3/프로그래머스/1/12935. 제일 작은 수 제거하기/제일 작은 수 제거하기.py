def solution(arr):
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]  
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    if len(arr) == 1:
        return [-1]

    sorted_arr = quick_sort(arr)

    min_val = sorted_arr[0]

    answer = [x for x in arr if x != min_val]
    return answer
