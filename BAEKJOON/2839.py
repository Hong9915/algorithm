N=int(input())

def min_sugar_bags(N):
    for five_kg_bags in range(N//5,-1,-1):
        remaining_weight = N -(five_kg_bags*5)
        if remaining_weight%3 == 0:
            three_kg_bags = remaining_weight//3
            return five_kg_bags + three_kg_bags
    return -1
print(min_sugar_bags(N))

# if(N%5==0):
#     print(N//5)
# elif(N%5==1):
#     if (N-5)<0:
#         print("-1")
#         exit()
#     print((N-5)//5+2)#?
# elif(N%5==2):
#     if (N-10)<0:
#         print("-1")
#         exit()
#     print((N-10)//5+4)
# elif(N%5==3):
#     print(N//5+1)
# elif(N%5==4):
#     if (N-5)<0:
#         print("-1")
#         exit()
#     print((N-5)//5+3)