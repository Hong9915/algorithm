"""
입차되고 출차된게 없으면 마지막에서 처리 
입차되고 출차되고 다시 입차됐을때를 알아야되기때문에 모든 record 다돌고 요금계산
차량은 uni하니까 defaultdict 번호 : 시간
visited로 출차된지 안된지 확인가능? 차량은 
"""
from collections import defaultdict

def solution(fees, records):
    b_t, b_f, d_t, d_f = fees
    dic = defaultdict(int)
    room = defaultdict(str)
    last_hour, last_min = 23,59
    
    for record in records:
        time,car_num,mov = record.split(" ")
        if mov == "IN": #
            room[car_num] = time
        elif mov == "OUT":
            in_time = room.pop(car_num)
            in_hour, in_min = in_time.split(":")
            out_hour , out_min = time.split(":")
            
            dur = (int(out_hour) - int(in_hour)) * 60 + (int(out_min) - int(in_min))
            
            dic[car_num] += dur
    
    for car_num, time in room.items():
        in_hour, in_min = time.split(":")
        
        dur = (int(last_hour) - int(in_hour)) * 60 + (int(last_min) - int(in_min))
        dic[car_num] += dur

    
    answer = []
    result = sorted(dic.items())

    for car_num, total_time in result:
        if total_time > b_t :
            fee = b_f + ((total_time - b_t + d_t - 1)//d_t)*d_f        
            answer.append(fee)
        else :
            answer.append(b_f)
 
    return answer