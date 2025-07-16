def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}

    for name in callings:
        i = rank[name]         
        players[i], players[i-1] = players[i-1], players[i] 
        rank[players[i]] = i
        rank[players[i-1]] = i - 1

    return players
