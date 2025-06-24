#메모리 초과
# def quick_sort(lst,num):
    
#     if len(lst) <= 1:
#         return lst
#     pivot = lst[len(lst)//2]
    
#     left=[x for x in lst if x < pivot]
#     middle=[x for x in lst if x==pivot]
#     right=[x for x in lst if x > pivot]
    
#     return quick_sort(left)+middle + quick_sort(right)
# N =int(input())
# result=[]
# for _ in range(N):
#     num=int(input())
#     result.append(num)

# result=quick_sort(result)

# print("\n".join(map(str,result)))
# sys input의 시간 효율이 더 좋음
import sys

def input():
    return sys.stdin.readline()

N=int(input())

counts=[0]*10001
for _ in range(N):
    counts[int(input())]+=1

for i in range(len(counts)):
    if counts[i]!=0:
        for _ in range(counts[i]):
            print(i)
#gpt코드
# import sys
# input = sys.stdin.read

# def count_sort(nums, max_val):
#     # 계수 배열을 생성합니다.
#     count = [0] * (max_val + 1)
    
#     # 각 숫자의 등장 횟수를 세어서 count 배열에 저장합니다.
#     for num in nums:
#         count[num] += 1
    
#     # 결과를 저장할 리스트를 만듭니다.
#     sorted_nums = []
    
#     # count 배열을 기반으로 정렬된 숫자를 저장합니다.
#     for num, freq in enumerate(count):
#         if freq > 0:
#             sorted_nums.extend([num] * freq)
    
#     return sorted_nums

# def main():
#     # 전체 입력을 한 번에 읽어옵니다.
#     data = input().split()
    
#     # 첫 번째 값은 숫자의 개수입니다.
#     N = int(data[0])
    
#     # 나머지 값들은 숫자들입니다.
#     nums = list(map(int, data[1:1 + N]))
    
#     # 최대 값은 10,000으로 주어졌습니다.
#     max_val = 10000
    
#     # 계수 정렬을 수행합니다.
#     sorted_nums = count_sort(nums, max_val)
    
#     # 결과를 출력합니다.
#     sys.stdout.write('\n'.join(map(str, sorted_nums)) + '\n')

# if __name__ == "__main__":
#     main()
