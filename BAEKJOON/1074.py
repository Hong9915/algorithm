#못품 
#gpt 코드
import sys
input = sys.stdin.readline

def Z(N, r, c):
    ans = 0  # 초기 방문 순서 카운터
    while N > 0:
        N -= 1  # 매 단계에서 N을 감소시켜 더 작은 부분으로 분할
        half = 2**N  # 현재 N에 대한 중간점 계산
        
        # 현재 위치가 첫 번째 사분면 (좌상단) 인 경우
        if r < half and c < half:
            pass  # 아무 작업도 필요 없음
        
        # 현재 위치가 두 번째 사분면 (우상단) 인 경우
        elif r < half and c >= half:
            ans += half * half  # 첫 번째 사분면을 지난 후의 순서를 더함
            c -= half  # 두 번째 사분면으로 이동
        
        # 현재 위치가 세 번째 사분면 (좌하단) 인 경우
        elif r >= half and c < half:
            ans += 2 * (half * half)  # 첫 번째와 두 번째 사분면을 지난 후의 순서를 더함
            r -= half  # 세 번째 사분면으로 이동
        
        # 현재 위치가 네 번째 사분면 (우하단) 인 경우
        else:
            ans += 3 * (half * half)  # 첫 번째, 두 번째, 세 번째 사분면을 지난 후의 순서를 더함
            r -= half  # 네 번째 사분면으로 이동
            c -= half  # 네 번째 사분면으로 이동

    return ans  # 최종 방문 순서 반환

# 입력 받기
N, r, c = map(int, input().split())
print(Z(N, r, c))  # 결과 출력
