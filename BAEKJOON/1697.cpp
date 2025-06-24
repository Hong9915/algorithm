#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int find_the_fastest_time(int subin, int brother) {
    if (subin >= brother) {
        return subin - brother;
    }

    const int MAX_POSITION = 100000;
    vector<bool> visited(MAX_POSITION + 1, false);
    queue<pair<int, int>> q;  // (현재 위치, 시간)
    q.push({subin, 0});
    visited[subin] = true;

    while (!q.empty()) {
        int current = q.front().first;
        int time = q.front().second;
        q.pop();

        if (current == brother) {
            return time;
        }

        int next_positions[3] = {current - 1, current + 1, current * 2};
        for (int i = 0; i < 3; ++i) {
            int next = next_positions[i];
            if (next >= 0 && next <= MAX_POSITION && !visited[next]) {
                visited[next] = true;
                q.push({next, time + 1});
            }
        }
    }

    return -1;  // 이 부분은 도달하지 않음
}

int main() {
    int N, K;
    cin >> N >> K;
    cout << find_the_fastest_time(N, K) << endl;
    return 0;
}
