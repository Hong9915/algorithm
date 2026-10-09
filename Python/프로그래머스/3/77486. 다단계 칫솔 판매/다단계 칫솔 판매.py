"""
referall에있는 사람들 부모 등록하고 defaultdict로 그다음에 seller 한명씩 돌면서 위로 끝까지 타고가기?
"""

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    N = len(enroll)
    X = len(seller)
    
    answer =[]
    profit = {}
    dic = {}
    for i in range(N):
        profit[enroll[i]] = 0
        dic[enroll[i]] = referral[i]
        
    for i in range(X):
        money = amount[i] * 100
        name = seller[i]

        while name != "-" and money > 0 :
            profit[name] += money - money//10
            name = dic[name]
            money = money//10


    return [profit[name] for name in enroll]