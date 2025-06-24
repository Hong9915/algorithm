#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int M, N;

bool check(const vector<vector<int>>& array) {
    for (int n = 0; n < N; ++n) {
        for (int m = 0; m < M; ++m) {
            if (array[n][m] == 0) {
                return false;
            }
        }
    }
    return true;
}

int bfs(vector<vector<int>>& array, vector<pair<int, int>>& start_box) {
    vector<int> up = {1, -1, 0, 0};
    vector<int> down = {0, 0, 1, -1};
    
    queue<pair<int, int>> q;
    for (const auto& pos : start_box) {
        q.push(pos);
    }

    int days = -1;
    while (!q.empty()) {
        ++days;
        int size = q.size();
        for (int i = 0; i < size; ++i) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            for (int d = 0; d < 4; ++d) {
                int nx = x + up[d];
                int ny = y + down[d];

                if (0 <= nx && nx < M && 0 <= ny && ny < N && array[ny][nx] == 0) {
                    array[ny][nx] = 1;
                    q.push({nx, ny});
                }
            }
        }
    }

    if (check(array)) {
        return days;
    } else {
        return -1;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> M >> N;

    vector<vector<int>> tomato_box(N, vector<int>(M));
    vector<pair<int, int>> start_box;

    for (int n = 0; n < N; ++n) {
        for (int m = 0; m < M; ++m) {
            cin >> tomato_box[n][m];
            if (tomato_box[n][m] == 1) {
                start_box.push_back({m, n});
            }
        }
    }

    if (start_box.size() == M * N) {
        cout << "0\n";
    } else {
        cout << bfs(tomato_box, start_box) << '\n';
    }

    return 0;
}
