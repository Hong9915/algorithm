results=[0]*42
for i in range(10):
    num=int(input())
    num=num%42
    results[num]=1

print(sum(results))
    
    