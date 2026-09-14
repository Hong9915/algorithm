def solution(friends, gifts):
    n = len(friends)
    name_to_index = {name: i for i, name in enumerate(friends)}
    
    give_table = [[0] * n for _ in range(n)]  
    gift_score = [0] * n  

    for gift in gifts:
        giver, receiver = gift.split()
        gi = name_to_index[giver]
        ri = name_to_index[receiver]
        give_table[gi][ri] += 1
        gift_score[gi] += 1
        gift_score[ri] -= 1

    next_gift = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            give_ij = give_table[i][j]
            give_ji = give_table[j][i]

            if give_ij > give_ji:
                next_gift[i] += 1
            elif give_ij == give_ji:
                if gift_score[i] > gift_score[j]:
                    next_gift[i] += 1

    return max(next_gift)
