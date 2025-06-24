alphabet = input().upper()
count = {}
for char in alphabet:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

max_count = 0
max_chars = []
for char, char_count in count.items():
    if char_count > max_count:
        max_count = char_count
        max_chars = [char]
    elif char_count == max_count:
        max_chars.append(char)

if len(max_chars) == 1:
    print(max_chars[0])
else:
    print("?")