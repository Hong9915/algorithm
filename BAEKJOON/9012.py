def check_VPS(str):
    result="NO"
    a=0
    b=0
    for word in str:
        if a < b:
            return result
        if word=="(":
            a+=1
        elif word==")":
            b+=1
    if a==b:
        result="YES"
        return result
    return result
N=int(input())
for _ in range(N):
    print(check_VPS(str(input())))