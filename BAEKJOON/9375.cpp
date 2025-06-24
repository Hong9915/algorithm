#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

// 가능한 조합의 수를 계산하는 함수
int outfit_cases(const unordered_map<string, vector<string>>& clothes) {
    int result = 1;
    for (const auto& pair : clothes) {
        result *= (pair.second.size() + 1); // 각 카테고리의 의상 수 + 1 (의상을 선택하지 않는 경우 포함)
    }
    return result - 1; // 최소한 하나의 의상은 선택해야 하므로 빈 경우를 제외하기 위해 1을 뺍니다.
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        unordered_map<string, vector<string>> clothes;
        int n;
        cin >> n;
        
        for (int i = 0; i < n; ++i) {
            string item, category;
            cin >> item >> category;
            clothes[category].push_back(item); // 각 카테고리에 의상을 추가
        }
        
        cout << outfit_cases(clothes) << endl;
    }

    return 0;
}
