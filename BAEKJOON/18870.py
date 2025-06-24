import sys

input = sys.stdin.readline

# 입력 처리
N = int(input().strip())
numbers = list(map(int, input().strip().split()))

# 중복 제거 및 정렬
sorted_unique_numbers = sorted(set(numbers))
print(sorted_unique_numbers)

# 좌표 압축을 위한 매핑 생성
coordinate_map = {value: index for index, value in enumerate(sorted_unique_numbers)}
# 결과 리스트 생성
compressed_numbers = [coordinate_map[x] for x in numbers]

# 결과 출력
print(" ".join(map(str, compressed_numbers)))
