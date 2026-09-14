def solution(keymap, targets):
    answer = []
    char_map = {}
    
    for key in keymap:
        for idx, char in enumerate(key):
            if char not in char_map:
                char_map[char] = idx + 1
            else:
                char_map[char] = min(char_map[char], idx + 1)

    for target in targets:
        total = 0
        for char in target:
            if char not in char_map:
                total = -1
                break
            total += char_map[char]
        answer.append(total)

    return answer
