#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// comparePairs 함수는 std::pair<int, int> 타입의 두 인자 a와 b를 받아,
// 두 쌍(pair)의 두 번째 원소(second)와 첫 번째 원소(first)를 기준으로 비교하여
// 정렬 순서를 결정하는 사용자 정의 비교 함수입니다.
bool comparePairs(const pair<int, int> &a, const pair<int, int> &b) {
    if (a.second == b.second) {
        return a.first < b.first; // second 값이 같을 경우, first 기준 정렬
    }
    return a.second < b.second; // 일반적인 경우, second 기준 정렬
}

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> time_line;
    for (int i = 0; i < N; i++) {
        int start, end;
        cin >> start >> end;
        time_line.push_back(make_pair(start, end));
    }

    // 벡터가 비어있을 때를 처리
    if (N == 0) {
        cout << 0 << endl;
        return 0;
    }

    // 사용자 정의 비교 함수를 사용하여 끝나는 시간 기준으로 정렬
    sort(time_line.begin(), time_line.end(), comparePairs);

    int end_time = time_line[0].second;
    int ans = 1;
    for (int i = 1; i < N; i++) {
        if (time_line[i].first >= end_time) {
            ans++;
            end_time = time_line[i].second;
        }
    }
    cout << ans << endl;

    return 0;
}
