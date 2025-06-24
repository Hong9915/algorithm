#include <iostream>
#include <vector>

using namespace std;

// 색종이를 재귀적으로 분할하여 색깔을 세는 함수
pair<int, int> colored_paper(int size, int x, int y, const vector<vector<int>>& paper) {
    int color = paper[x][y];
    bool all_same = true;

    for (int i = x; i < x + size; i++) {
        for (int j = y; j < y + size; j++) {
            if (paper[i][j] != color) {
                all_same = false;
                break;
            }
        }
        if (!all_same) break;
    }

    if (all_same) {
        if (color == 0) return {1, 0}; // 흰색
        else return {0, 1}; // 검은색
    } else {
        int half = size / 2;
        pair<int, int> white_black1 = colored_paper(half, x, y, paper);
        pair<int, int> white_black2 = colored_paper(half, x, y + half, paper);
        pair<int, int> white_black3 = colored_paper(half, x + half, y, paper);
        pair<int, int> white_black4 = colored_paper(half, x + half, y + half, paper);
        
        int white = white_black1.first + white_black2.first + white_black3.first + white_black4.first;
        int black = white_black1.second + white_black2.second + white_black3.second + white_black4.second;
        return {white, black};
    }
}

int main() {
    int N;
    cin >> N;
    vector<vector<int>> paper(N, vector<int>(N));

    // 종이의 색깔 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> paper[i][j];
        }
    }

    pair<int, int> result = colored_paper(N, 0, 0, paper);
    cout << result.first << endl; // 흰색 종이의 수
    cout << result.second << endl; // 검은색 종이의 수

    return 0;
}
