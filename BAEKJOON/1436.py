N=int(input())
count=0
world_end_num=666
while(1):
    
    if  '666'in str(world_end_num):
        count+=1
        if (count == N):
            print(world_end_num)
            break
            
    world_end_num+=1
