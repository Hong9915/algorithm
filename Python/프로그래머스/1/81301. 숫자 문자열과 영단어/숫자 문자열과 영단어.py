def solution(s):
    answer = ""
    
    word_to_num = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
    }
    
    temp = ""
    for st in s:
        if st.isdigit():
            answer += st
            continue
        temp += st
        if temp in word_to_num:
            answer += str(word_to_num[temp])
            temp = ""

        
        

    return int(answer)