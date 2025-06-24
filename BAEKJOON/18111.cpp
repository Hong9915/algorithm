#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int N, M, B;
    cin >> N >> M >> B;  // 세로 N, 가로 M, 인벤토리 블록 수 B 입력

    vector<vector<int>> land(N, vector<int>(M));

    // 땅 높이 입력
    int min_height = 256, max_height = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> land[i][j];
            min_height = min(min_height, land[i][j]);
            max_height = max(max_height, land[i][j]);
        }
    }

    int min_time = INT_MAX;  // 최소 시간을 무한대로 초기화
    int best_height = 0;     // 최적의 높이

    // 가능한 모든 높이(최소 높이 ~ 최대 높이)에 대해 검사
    for (int target_height = min_height; target_height <= max_height; ++target_height) {
        int time = 0;
        int inventory = B;  // 인벤토리에 남은 블록 수

        // 땅의 모든 좌표에 대해 작업 수행
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                int current_height = land[i][j];

                if (current_height > target_height) {
                    // 블록 제거 (2초 소모, 인벤토리에 블록 추가)
                    int blocks_to_remove = current_height - target_height;
                    time += blocks_to_remove * 2;
                    inventory += blocks_to_remove;
                } else if (current_height < target_height) {
                    // 블록 추가 (1초 소모, 인벤토리에서 블록 사용)
                    int blocks_to_add = target_height - current_height;
                    time += blocks_to_add;
                    inventory -= blocks_to_add;
                }
            }
        }

        // 인벤토리에 블록이 충분한 경우에만 처리
        if (inventory >= 0) {
            // 최소 시간 갱신
            if (time < min_time) {
                min_time = time;
                best_height = target_height;
            } else if (time == min_time && target_height > best_height) {
                // 시간이 같을 경우 더 높은 높이를 선택
                best_height = target_height;
            }
        }
    }

    // 최소 시간과 최적의 높이 출력
    cout << min_time << " " << best_height << endl;

    return 0;
}
