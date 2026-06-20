from collections import defaultdict

def solution(gems):
    # 전체 보석 종류 수
    kind = len(set(gems))

    # 현재 구간에 포함된 보석 개수 저장
    cnt = defaultdict(int)

    # 투 포인터의 왼쪽 끝
    left = 0

    # 정답 구간 (초기값은 전체 구간)
    answer = [0, len(gems) - 1]

    # right를 한 칸씩 늘려가며 구간 확장
    for right in range(len(gems)):
        # 현재 보석 추가
        cnt[gems[right]] += 1

        # 현재 구간에 모든 종류의 보석이 포함된 경우
        while len(cnt) == kind:

            # 현재 구간이 더 짧다면 정답 갱신
            if answer[1] - answer[0] > right - left:
                answer = [left, right]

            # 왼쪽 보석 제거
            cnt[gems[left]] -= 1

            # 개수가 0이 되면 딕셔너리에서 삭제
            # len(cnt)가 현재 보석 종류 수를 의미하도록 유지
            if cnt[gems[left]] == 0:
                del cnt[gems[left]]

            # 구간 축소
            left += 1

    # 문제는 1번 인덱스부터 시작하므로 +1
    return [answer[0] + 1, answer[1] + 1]