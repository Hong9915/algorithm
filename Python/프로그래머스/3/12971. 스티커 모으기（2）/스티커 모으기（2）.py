def solution(sticker):
    if len(sticker) == 1 or len(sticker) == 2:
        return max(sticker)
    dp_1 = [0] * len(sticker)
    dp_2 = [0] * len(sticker)
    
    for i in range(len(sticker)-1) :
        dp_1[i] = sticker[i] + max(dp_1[i-2], dp_1[i-3])
    for i in range(1,len(sticker)) :
        dp_2[i] = sticker[i] + max(dp_2[i-2], dp_2[i-3])
    
    max_1 = max(dp_1)
    max_2 = max(dp_2)
    
    answer = max(max_1,max_2)

    

    return answer