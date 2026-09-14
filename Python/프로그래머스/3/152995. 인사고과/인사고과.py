def solution(scores):
    wanho = scores[0]
    wanho_idx = 0  

    scores_with_index = [(att, peer, i) for i, (att, peer) in enumerate(scores)]
    scores_with_index.sort(key=lambda x: (-x[0], x[1]))

    max_peer = 0
    qualified = []

    for att, peer, i in scores_with_index:
        if peer >= max_peer:
            qualified.append((att, peer, i))
            max_peer = max(max_peer, peer)

    if not any(i == wanho_idx for _, _, i in qualified):
        return -1

    qualified.sort(key=lambda x: -(x[0] + x[1]))

    rank = 1
    prev_score = qualified[0][0] + qualified[0][1]
    same = 1

    for j, (att, peer, i) in enumerate(qualified):
        total = att + peer

        if j == 0:
            if i == wanho_idx:
                return rank
            continue

        if total < prev_score:
            rank += same
            same = 1
            prev_score = total
        else:
            same += 1

        if i == wanho_idx:
            return rank

    return -1
