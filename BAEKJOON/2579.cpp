#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> steps(N);
    for (int i = 0; i < N; i++) {
        cin >> steps[i];
    }

    // dp 배열을 사용하여 최대 점수를 저장할 것임
    vector<int> dp(N);

    // 계단이 1개인 경우
    if (N == 1) {
        cout << steps[0] << endl;
        return 0;
    }
    
    // 계단이 2개인 경우
    if (N == 2) {
        cout << steps[0] + steps[1] << endl;
        return 0;
    }

    // 초기 상태 설정
    dp[0] = steps[0];
    dp[1] = steps[0] + steps[1];

    // DP를 이용하여 최대 점수 계산
    for (int i = 2; i < N; i++) {
        // 현재 계단을 밟는 두 가지 경우:
        // 1. 두 계단 전에서 현재 계단으로 이동
        // 2. 한 계단 전에서 현재 계단으로 이동, 단 이전에 두 계단 전에서 현재 계단 전으로 왔음
        dp[i] = max(dp[i - 2] + steps[i], steps[i - 1] + dp[i - 3] + steps[i]);
    }

    // 마지막 계단에서의 최대 점수 출력
    cout << dp[N - 1] << endl;

    return 0;
}
