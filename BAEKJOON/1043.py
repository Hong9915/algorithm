#gpt
import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

x = list(map(int, input().strip().split()))
truth_num_person = x[0]
truth_person = x[1:]  
parties = [] 

for _ in range(M):
    x = list(map(int, input().strip().split()))
    parties.append(x[1:])  

# 진실 전파
changed = True
while changed:
    changed = False
    for party in parties:
        if any(person in truth_person for person in party):
            for person in party:
                if person not in truth_person:
                    truth_person.append(person)
                    changed = True

# 거짓말할 수 있는 파티 수 계산
count = 0
for party in parties:
    if not any(person in truth_person for person in party):
        count += 1

print(count)
