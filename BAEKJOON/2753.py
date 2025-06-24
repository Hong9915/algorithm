year = int(input())

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("1")
            exit()
        print("0")
        exit()
    print("1")
    exit()
else :
    print("0")
        