def knapsack(N, K, weights, values):
    dp = [[0] * (K + 1) for _ in range(N + 1)]  # 배낭 문제를 해결하기 위한 DP 테이블 초기화
    for i in range(1, N + 1):  # 각 물건에 대하여
        weight = weights[i - 1]  # i번째 물건의 무게
        value = values[i - 1]  # i번째 물건의 가치
        for j in range(1, K + 1):  # 배낭의 무게에 따라
            if j >= weight:  # 현재 물건을 배낭에 넣을 수 있는 경우
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)  # 최댓값을 선택하여 DP 테이블 갱신
            else:  # 현재 물건을 배낭에 넣을 수 없는 경우
                dp[i][j] = dp[i - 1][j]  # 이전 상태를 그대로 가져옴
    return dp[N][K]  # 배낭에 넣을 수 있는 물건들의 가치의 최댓값 반환


# 입력 받기
N, K = map(int, input().split())  # 물품의 수 N과 배낭의 무게 제한 K 입력
weights = []  # 각 물건의 무게를 저장할 리스트
values = []  # 각 물건의 가치를 저장할 리스트

for _ in range(N):
    w, v = map(int, input().split())  # 물건의 무게와 가치 입력
    weights.append(w)  # 무게 리스트에 추가
    values.append(v)  # 가치 리스트에 추가

# 배낭 문제 풀기
max_value = knapsack(N, K, weights, values)  # 배낭 문제 함수 호출하여 최대 가치 계산

# 결과 출력
print(max_value)  # 최대 가치 출력

# N ,K,*l=map(int,open(0).read().split())
# d=-~K*[0]
# while l:
#  w,v,*l=l
#  for i in range(K,w-1,-1):d[i]=max(d[i],d[i-w]+v)
# print(d[K])
