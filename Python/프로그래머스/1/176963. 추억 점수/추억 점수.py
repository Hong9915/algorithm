def solution(name, yearning, photo):
    yearning_dict = {}
    for i in range(len(name)):
        yearning_dict[name[i]] = yearning[i]

    answer = []

    for i in range(len(photo)):
        memory_score = 0
        
        for person in photo[i]:
    
            memory_score += yearning_dict.get(person, 0)
        
        answer.append(memory_score)
    
    return answer
