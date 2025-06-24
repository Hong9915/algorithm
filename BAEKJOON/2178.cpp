#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// 미로의 크기 (N: 세로 길이, M: 가로 길이)
int N, M;

// 방향을 나타내는 배열 (상, 하, 좌, 우)
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

// 미로와 방문 여부를 저장하는 벡터
vector<vector<int>> mirro;
vector<vector<int>> dist;

int bfs(int startY, int startX) {
    // BFS 탐색을 위한 큐 (큐의 요소는 (y, x) 좌표)
    queue<pair<int, int>> q;

    // 시작 지점을 큐에 추가하고, 시작 지점의 거리를 1로 설정
    q.push({startY, startX});
    dist[startY][startX] = 1;

    // 큐가 빌 때까지 반복
    while (!q.empty()) {
        // 큐에서 현재 위치를 꺼냄
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        // 네 방향(상, 하, 좌, 우)으로 이동을 시도
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i]; // 이동할 새로운 x좌표
            int ny = y + dy[i]; // 이동할 새로운 y좌표

            // 좌표가 미로의 범위를 벗어나지 않는지 확인
            if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
                // 이동할 수 있는 길인지 확인 (mirro[ny][nx] == 1)하고, 아직 방문하지 않은 곳(dist[ny][nx] == -1)인지 확인
                if (mirro[ny][nx] == 1 && dist[ny][nx] == -1) {
                    dist[ny][nx] = dist[y][x] + 1; // 새로운 위치의 거리를 현재 거리 + 1로 설정
                    q.push({ny, nx}); // 큐에 새로운 위치를 추가
                }
            }
        }
    }

    // 도착 지점의 거리를 반환 (도착 지점은 (N-1, M-1))
    return dist[N-1][M-1];
}

int main() {
    // 미로의 크기를 입력받음
    cin >> N >> M;

    // 미로와 거리 배열을 초기화
    mirro = vector<vector<int>>(N, vector<int>(M));
    dist = vector<vector<int>>(N, vector<int>(M, -1));

    // 미로의 각 줄을 입력받음
    for (int i = 0; i < N; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < M; j++) {
            mirro[i][j] = line[j] - '0'; // '0'을 빼서 정수로 변환
        }
    }

    // BFS를 사용하여 최단 거리를 계산
    int result = bfs(0, 0);

    // 결과 출력
    cout << result << endl;

    return 0;
}
