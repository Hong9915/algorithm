num=0
while(True):
    num=str(input())
    if (num=='0'):
        break
    count=0
    for i in range((len(num)//2)):
        if (num[i]!=num[-i-1]):
            print("no")
            break
        else:
            count+=1
    if (count==len(num)//2):
        print("yes")