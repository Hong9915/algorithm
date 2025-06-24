# import sys
# input = sys.stdin.readline

# # 입력 처리
# N = int(input())
# numbers = list(map(int, input().strip().split()))

# # DP 배열 초기화
# left = [1] * N  # 증가 부분 수열 길이
# right = [1] * N  # 감소 부분 수열 길이

# # 증가하는 부분 수열 계산
# for i in range(N):
#     for j in range(i):
#         if numbers[i] > numbers[j]:
#             left[i] = max(left[i], left[j] + 1)

# # 감소하는 부분 수열 계산 (뒤에서부터)
# for i in range(N - 1, -1, -1):
#     for j in range(N - 1, i, -1):
#         if numbers[i] > numbers[j]:
#             right[i] = max(right[i], right[j] + 1)

# # 바이토닉 부분 수열의 최댓값 계산
# max_length = 0
# for i in range(N):
#     max_length = max(max_length, left[i] + right[i] - 1)

# # 결과 출력
# print(max_length)


def lis_with_binary_search(nums):
    dp = []
    lis_length = [0] * len(nums)

    def binary_search(dp, target):
        """이진 탐색으로 target의 위치 찾기"""
        low, high = 0, len(dp) - 1
        while low <= high:
            mid = (low + high) // 2
            if dp[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    for i, num in enumerate(nums):
        pos = binary_search(dp, num)  # num이 들어갈 위치를 찾음
        if pos == len(dp):
            dp.append(num)  # num을 dp에 추가
        else:
            dp[pos] = num  # num으로 기존 값 대체
        lis_length[i] = pos + 1  # 현재 LIS 길이 기록
        print(dp)

    return lis_length

# 입력 처리
import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().strip().split()))

# 증가하는 부분 수열(LIS) 계산
left = lis_with_binary_search(numbers)

# 감소하는 부분 수열(LDS) 계산 (역순으로 처리)
right = lis_with_binary_search(numbers[::-1])[::-1]

# 바이토닉 부분 수열 길이 계산
max_length = max(left[i] + right[i] - 1 for i in range(N))

# 결과 출력
print(max_length)
