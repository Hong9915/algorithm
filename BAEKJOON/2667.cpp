#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<vector<int>> grid;
vector<vector<bool>> visited;

// 방향 벡터: 상, 하, 좌, 우
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int dfs(int x, int y) {
    // 스택을 이용한 DFS
    vector<pair<int, int>> stack;
    stack.push_back({x, y});
    int count = 0;
    
    while (!stack.empty()) {
        int cx = stack.back().first;
        int cy = stack.back().second;
        stack.pop_back();
        
        if (!visited[cx][cy]) {
            visited[cx][cy] = true;
            count++;
            
            for (int i = 0; i < 4; ++i) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && grid[nx][ny] == 1) {
                    stack.push_back({nx, ny});
                }
            }
        }
    }
    
    return count;
}

int main() {
    // 입력 처리
    cin >> N;
    grid.resize(N, vector<int>(N));
    visited.resize(N, vector<bool>(N, false));
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            scanf("%1d", &grid[i][j]);
        }
    }

    // 단지 정보 수집
    vector<int> complex_sizes;
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (grid[i][j] == 1 && !visited[i][j]) {
                int size = dfs(i, j);
                complex_sizes.push_back(size);
            }
        }
    }
    
    // 결과 출력
    sort(complex_sizes.begin(), complex_sizes.end());
    cout << complex_sizes.size() << endl;
    for (int size : complex_sizes) {
        cout << size << endl;
    }
    
    return 0;
}
