def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        timelog=timelogs[i]
        hour=schedules[i]//100
        minutes=schedules[i]%100
        success=1
        for day in range(7):
            if (startday+day-1)%7>=5 :
                continue
            time=timelog[day]
            start_hour=time//100
            start_minute=time%100
            if (start_hour < hour):
                continue
            if (hour+1)==start_hour :
                start_minute+=60        
            if (start_hour == hour and start_minute <= minutes + 10):
                continue
            elif (start_hour == hour + 1 and start_minute <= minutes +10):
                continue
            print(i,(startday-1+day)%7)
            success-=1
            break
        answer+=success
    
    return answer