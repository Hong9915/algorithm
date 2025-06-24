palindrome=input()
a = True
for i in range(palindrome.__len__()//2):
    if (palindrome[i]!=palindrome[-(i+1)]):
        a = False
if (a):
    print("1")
else :
    print("0")