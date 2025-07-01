def solution(cap, n, deliveries, pickups):
    delivery=0
    pickup=0
    result=0
    for i in range (n-1,-1,-1) :
        delivery+=deliveries[i]
        pickup+=pickups[i]
        while delivery > 0 or pickup > 0:            
            delivery-=cap
            pickup-=cap
            result+=(i+1)*2
            
    
    answer = result
    return answer