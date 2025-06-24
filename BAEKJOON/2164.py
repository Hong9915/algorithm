from collections import deque
N=int(input())
card=deque([i+1 for i in range(N)])

    
while(card):
    if len(card)==1:
        print(card.popleft())
        break
    card.popleft()
    temp_card=card.popleft()
    card.append(temp_card)
    
# 블로그에서 가져온거 규칙을 찾아서 함 [ INPUT - 2**(INPUT>2의 제곱) ] * 2이다. 훨씬더 시간 단축이됌
# input = int(input())
# square = 2

# while True:
#     if (input == 1 or input == 2):
#         print(input)
#         break
#     square *= 2
#     if (square >= input):
#         print((input - (square // 2)) * 2)
#         break
