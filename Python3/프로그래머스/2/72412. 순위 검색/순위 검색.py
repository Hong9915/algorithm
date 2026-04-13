import bisect

def solution(info, query):
    db = {}
    answer = []
    for word in info:
        lan, job, exp, food, score = word.split(" ")
        conditions = [lan, job, exp, food] 
        
        for i in range(2**4):  
            key = []
            for j in range(4):
                if i & (1 << j):  
                    key.append(conditions[j])
                else:           
                    key.append("-")
            
            key = tuple(key) 
            if key not in db:
                db[key] = []
            db[key].append(int(score))
    
    for key in db:
        db[key].sort()
    
    for word in query:
        query_score = word.rsplit(" ", 1)
        query1 = tuple(query_score[0].split(" and "))
        
        if query1 in db:
            tmp = db[query1]
            idx = bisect.bisect_left(tmp, int(query_score[1])) 
            answer.append(len(tmp) - idx)
        else:
            answer.append(0)
                
    return answer