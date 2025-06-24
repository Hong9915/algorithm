H , M = map(int, input().split())

M -= 45
if M >= 0:
    print(H, M)
else:
    H-=1
    if H < 0:
        print("23" , 60+M)
    else:
        print(H,60+M)