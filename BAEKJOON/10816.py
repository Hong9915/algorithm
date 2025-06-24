N=int(input())
cards={}
N_cards=list(map(int,input().split()))
M=int(input())
M_cards=list(map(int,input().split()))
result=[]


for card in N_cards:
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1

for card in M_cards:
    if card in cards:
        result.append(cards[card])
    else:
        result.append(0)

print(' '.join(map(str, result)))