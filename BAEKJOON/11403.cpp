#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void bfs(const vector<vector<int>>& array, vector<vector<int>>& result, int N) {
    for (int i = 0; i < N; ++i) {
        vector<bool> visited(N, false);
        queue<int> q;
        q.push(i);

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            for (int j = 0; j < N; ++j) {
                if (array[node][j] == 1 && !visited[j]) {
                    visited[j] = true;
                    result[i][j] = 1;
                    q.push(j);
                }
            }
        }
    }
}

int main() {
    int N;
    cin >> N;

    vector<vector<int>> array(N, vector<int>(N));
    vector<vector<int>> result(N, vector<int>(N, 0));

    // 입력받은 인접 행렬을 저장
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> array[i][j];
        }
    }

    // BFS를 통해 각 노드에서 다른 노드로의 연결 여부를 확인
    bfs(array, result, N);

    // 결과 출력
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
