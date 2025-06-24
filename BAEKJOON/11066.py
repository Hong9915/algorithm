test_num = int(input())

for _ in range (test_num):
    num = int(input())
    lst = list(map(int,input().split()))
    lst_dp = [[0]*(num) for _ in range (num)] # num 길이의 2차원 배열 생성
    
    for i in range(num-1):
        lst_dp[i][i+1] = lst[i]+lst[i+1] #lst_dp[i][j]에는 리스트의 i부터 i+1을 더한 값을 갖게 된다
        # for item in (lst_dp):
        #     print(item)
        for j in range(i+2,num):
            lst_dp[i][j] = lst_dp[i][j-1] + lst[j]
            # for item in (lst_dp):
            #     print(item)
    for item in (lst_dp):
        print(item)
    for d in range (2,num):
        for i in range(num-d):
            j = d + i
            minimum = [lst_dp[i][k] + lst_dp[k+1][j] for k in range(i,j)]
            lst_dp[i][j] += min(minimum)
            
    print(lst_dp[0][num-1])