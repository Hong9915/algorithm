"""
4g기지국에는 5g 기지국이 설치
W만큼 전파거리가 생김

내흐름은 vistied = [False] * N 짜리 만들어서 stations돌리고 visited[stations[i-W:i+W+1]] 원은아니니까 0이상 N이하 체크하고 다 True로 만들고
1부터 시작해서 N 까지 vistied확인하면서 False면 하나뒤로 이동하고 W가됐을때까지 False면 기지국 설치 True면 한칸뒤에 설치
"""
def solution(n, stations, w):
    A = []
    tmp = 1
    answer = 0
    
    for station in stations:
        if station - w <= 1 :
            A.append([1,station+w])
            continue 
    
        if station + w >= n :
            A.append([station-w,n])
            break
        
        A.append([station-w,station+w])

    
    for start, end in A:
        if start - tmp > 0 :
            answer += (start - tmp) // (2*w + 1)
            if (start - tmp) % (2*w + 1):
                answer+=1
        if end == n :
            tmp = end
            break
        tmp = end + 1
        
    if tmp != end:
        answer += (n - tmp + 1) // (2*w +1)
        if (n - tmp + 1) % (2*w + 1):
                answer+=1

    

    return answer