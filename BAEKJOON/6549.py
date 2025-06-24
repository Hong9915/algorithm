from sys import stdin


while True:
    graph = list(map(int, stdin.readline().split())) #한줄씩 읽어서 리스트 타입으로 그래프를 만듦
    
    # 0이 입력되면 반복문을 종료합니다.
    if graph[0] == 0: 
        break

    # 스택과 최대 직사각형 넓이를 저장할 변수를 초기화합니다.
    stack = []
    max_result = 0
    for i, height in enumerate(graph): #그래프 크기만큼 반복
        if i == 0:  # 첫 번째 i는 막대기의 개수를 의미하므로 넘어갑니다. 
            continue

        # 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 작으면
        if stack and stack[-1][1] > height: #스택이 비어있지 않고 마지막으로 들어온 스택이 현재 막대기보다 높다면
            while stack:  # 스택에서 빼내며 최대 직사각형 넓이를 계산합니다.
                stack_i, stack_height = stack.pop() #가장 마지막으로 들어온 스택을 빼냄
                width_start = 1 # 너비를 1로 초기화
                if stack: # 만약 스택이 비어있다면 너비가 2가 아닌 1이 될테니
                    width_start = stack[-1][0]+1 # stack[-1][0]은 마지막 스택의 위치를 알려줌
                result = (i - width_start) * stack_height
                max_result = max(result, max_result) # 최대값 갱신
                # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산합니다.
                if not stack or stack[-1][1] <= height:
                    break

     
        if not stack or stack[-1][1] <= height: # 스택이 비었거나 마지막으로 들어온 스택이 현재 순회하고있는 높이보다 작다면
            stack.append((i, height))  # 스택에 현재 막대기를 추가합니다.

    # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산합니다. 이유 1.스택에 더 이상 비교할 막대기가 남아있는 경우 2.현재 순회하고 있는 막대기가 스택의 마지막 막대기보다 작은 경우
    while stack:
        stack_i, stack_height = stack.pop()
        width_start = 1
        if stack:
            width_start = stack[-1][0]+1
        result = (graph[0]+1 - width_start) * stack_height
        max_result = max(result, max_result) # 최대값 갱신

    # 최대 직사각형 넓이를 출력합니다.
    print(max_result)
