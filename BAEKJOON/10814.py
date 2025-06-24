def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[len(lst)//2][0]  # 나이를 기준으로 피벗을 설정
    
    left = [x for x in lst if x[0] < pivot]    # 피벗보다 작은 나이들
    middle = [x for x in lst if x[0] == pivot]  # 피벗과 같은 나이들
    right = [x for x in lst if x[0] > pivot]   # 피벗보다 큰 나이들
    
    return quick_sort(left) + middle + quick_sort(right)

N = int(input())  # 회원 수 입력
clients = []

for _ in range(N):
    age, name = input().strip().split()  # 나이와 이름을 공백으로 분리하여 입력 받음
    age = int(age)  # 나이는 정수형으로 변환
    clients.append((age, name))  # 튜플 형태로 리스트에 추가

# 나이를 기준으로 오름차순 정렬
sorted_clients = quick_sort(clients)

# 정렬된 결과를 출력
for client in sorted_clients:
    print(client[0], client[1])
