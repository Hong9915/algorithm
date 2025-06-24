N=int(input())

test_score=list(map(int,input().split()))

max_score=max(test_score)
result_score=[]
for score in test_score :
    result_score.append(score/max_score*100)
    

print(sum(result_score)/len(result_score))