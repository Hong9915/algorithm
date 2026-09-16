from collections import defaultdict

def solution(tickets):
    
    dic = defaultdict(list)
    
    for ap1, ap2 in tickets:
        dic[ap1].append(ap2)
    
    for key in dic:
        dic[key].sort()


    answer = []
    
    def dfs(ap) :
        if len(answer) == len(tickets)+1:
            return True
        
        for i in range(len(dic[ap])): # dict 별로 False는 지나고 나머지는 answer에 넣고 dic에는 False로 티켓 방문 표시
            if dic[ap][i] == False:
                continue
            
            next_ap = dic[ap][i]
            
            dic[ap][i] = False
            answer.append(next_ap)
            
            if dfs(next_ap):
                return True

            dic[ap][i] = next_ap
            answer.pop()


            
            
    answer.append("ICN")
    dfs("ICN")


    return answer