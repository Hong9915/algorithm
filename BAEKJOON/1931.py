import sys
input=sys.stdin.readline

N=int(input().strip())
time_line=[]
for _ in range (N):
    start, end = map (int,input().strip().split())
    time_line.append((start,end))
    
time_line.sort(key=lambda x: (x[1],x[0]))

count=1

end= time_line[0][1]
for i in range(1,N):
    if time_line[i][0] >= end:
        end= time_line[i][1]
        count+=1

print(count)