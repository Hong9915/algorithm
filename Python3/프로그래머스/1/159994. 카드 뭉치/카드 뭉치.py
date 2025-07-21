def solution(cards1, cards2, goal):
    answer = [] 
    i, j = 0, 0 

    for word in goal:
        if i < len(cards1) and cards1[i] == word:
            answer.append(cards1[i])
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            answer.append(cards2[j])
            j += 1
        else:
            return "No"
    
    return "Yes"

