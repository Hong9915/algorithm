def solution(message, spoiler_ranges):
    n = len(message)

    is_spoiler = [False] * n
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            is_spoiler[i] = True
    
    words = []
    i = 0
    while i < n:
        if message[i] != " ":
            j = i
            while j < n and message[j] != " ":
                j += 1

            words.append((message[i:j], i, j-1))
            i = j
        else:
            i += 1
    
    spoiled_words = set()
    not_spoiled_words = set()
    
    for word in words:
        wo, start, end = word
        if any(is_spoiler[i] for i in range(start,end+1)):
            spoiled_words.add(wo)
        else:
            not_spoiled_words.add(wo)
    print(spoiled_words)
    
    print(not_spoiled_words)
    answer = 0
    
    for spoiled_word in list(spoiled_words):
        if spoiled_word not in list(not_spoiled_words):
            answer+=1

        
        
    
    return answer