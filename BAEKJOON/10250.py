T = int(input())  # 테스트 케이스의 수

for _ in range(T):
    H, W, N = map(int, input().split())  # 각 테스트 케이스의 입력값 받기
    
    Y = N % H  
    X = N // H + 1  
    
    if Y == 0:
        Y = H
        X -= 1
    
    room_number = Y * 100 + X  # 방 번호 계산
    print(room_number)
