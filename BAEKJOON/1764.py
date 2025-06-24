import sys
input=sys.stdin.readline

N,M=map(int,input().strip().split())
no_listened=[]
no_seen=[]
def find_no_listend_seen(lst_1,lst_2):
    result=[]
    for x in lst_1:
        for y in lst_2:
            if x==y:
                result.append(x)
                
    return result
for _ in range (N):
    no_listened.append(input().strip())

for _ in range (M):
    no_seen.append(input().strip())
    

result=find_no_listend_seen(no_listened,no_seen)
result=sorted(result)
print(len(result))
for item in result:
    print(item)