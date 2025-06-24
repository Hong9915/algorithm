import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
M = int(input())
B = list(map(int, input().strip().split()))

def sol(arr1, arr2, res=None):
    if res is None:
        res = []
    
    if not arr1 or not arr2:
        return res
    
    m_arr1 = max(arr1)
    m_arr2 = max(arr2)
    index_arr1, index_arr2 = arr1.index(m_arr1), arr2.index(m_arr2)

    if m_arr1 == m_arr2:
        res.append(m_arr1)
        return sol(arr1[index_arr1 + 1:], arr2[index_arr2 + 1:], res)
    elif m_arr1 > m_arr2:
        arr1.pop(index_arr1)
        return sol(arr1, arr2, res)
    else:
        arr2.pop(index_arr2)
        return sol(arr1, arr2, res)

result = sol(A, B)
print(len(result))

print(" ".join(map(str,result)))

