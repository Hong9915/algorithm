def solution(s, skip, index):
    result = ''
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    for ch in s:
        current_index = alphabet.index(ch)
        new_index = (current_index + index) % len(alphabet)
        result += alphabet[new_index]

    return result
