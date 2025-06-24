def printer_queue(N,M,priorty):
    result=[]
    count=0
    for i in range (N):
        result.append([i,priorty[i]])
    
    while(result):
        max=result[0][1]
        for i in range(len(result)):
            if max < result[i][1]:
                max=result[i][1]
        for i in range(len(result)):
            if max > result[i][1]:
                result.append(result[i])
                del result[i]
                break
            elif max == result[i][1]: 
                count+=1
                if result[i][0] == M:
                    return count
                del result[i]
                break


test_case=int(input())

for _ in range(test_case):
    N , M =map(int,input().split())
    prioirties=list(map(int,input().split()))
    print(printer_queue(N,M,prioirties))

#gpt 코드
# def print_order(N, M, priorities):
    # # 주어진 N개의 문서와 M번째 문서의 인덱스, 그리고 각 문서의 중요도를 인자로 받습니다.
    # from collections import deque
    
    # # 각 문서의 인덱스와 중요도를 튜플 형태로 저장한 큐를 생성합니다.
    # queue = deque([(i, int(priorities[i])) for i in range(N)])
    
    # # 인쇄된 문서의 순서를 저장할 변수를 초기화합니다.
    # print_order = 0
    
    # # 큐가 비어있지 않은 동안 반복합니다.
    # while queue:
    #     # 큐의 맨 앞에 있는 문서를 꺼내서 current에 저장합니다.
    #     current = queue.popleft()
        
    #     # 큐의 나머지 문서 중에 current 문서보다 높은 중요도를 가진 문서가 있는지 확인합니다.
    #     if any(current[1] < q[1] for q in queue):
    #         # 높은 중요도를 가진 문서가 있다면 current 문서를 다시 큐의 맨 뒤로 보냅니다.
    #         queue.append(current)
    #     else:
    #         # 그렇지 않으면 current 문서를 인쇄합니다.
    #         print_order += 1
    #         # 인쇄한 문서가 우리가 찾는 M번째 문서라면 그 순서를 반환합니다.
    #         if current[0] == M:
    #             return print_order

# # 테스트케이스의 수를 입력받습니다.
# T = int(input())

# for _ in range(T):
#     N, M = map(int, input().split())
#     priorities = list(map(int, input().split()))
#     print(print_order(N, M, priorities))
