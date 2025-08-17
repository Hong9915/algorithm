def solution(numbers, hand):
    pos = {
        0: (3, 1),
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    left_pos = (3, 0)
    right_pos = (3, 2)

    result = ""

    for num in numbers:
        if num in [1, 4, 7]: 
            result += "L"
            left_pos = pos[num]
        elif num in [3, 6, 9]: 
            result += "R"
            right_pos = pos[num]
        else:
            l_dist = abs(left_pos[0] - pos[num][0]) + abs(left_pos[1] - pos[num][1])
            r_dist = abs(right_pos[0] - pos[num][0]) + abs(right_pos[1] - pos[num][1])

            if l_dist < r_dist:
                result += "L"
                left_pos = pos[num]
            elif r_dist < l_dist:
                result += "R"
                right_pos = pos[num]
            else: 
                if hand == "right":
                    result += "R"
                    right_pos = pos[num]
                else:
                    result += "L"
                    left_pos = pos[num]

    return result


