ascending="12345678"
descending="87654321"
result=""
N= list(map(int,input().split()))

for num in N:
    result+=str(num)

if ascending==result:
    print("ascending")
elif descending==result:
    print("descending")
else :
    print("mixed")

