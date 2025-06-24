#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    cin.ignore(); // 버퍼에 남은 개행문자 제거

    set<string> no_listened;
    set<string> no_seen;

    // 듣지 못한 사람들 명단 입력받기
    for (int i = 0; i < N; ++i) {
        string name;
        getline(cin, name);
        no_listened.insert(name);
    }

    // 보지 못한 사람들 명단 입력받기
    for (int i = 0; i < M; ++i) {
        string name;
        getline(cin, name);
        no_seen.insert(name);
    }
// const: 요소를 수정하지 않겠다는 의미입니다. 루프 내부에서 요소를 변경하지 않도록 보장합니다.
// auto: 요소의 타입을 자동으로 추론합니다. no_listened의 요소 타입이 std::string이므로 auto는 std::string으로 추론됩니다.
// &: 요소를 참조로 가져옵니다. 요소를 복사하지 않고 참조로 처리하여 성능을 향상시킵니다.
     // 교집합 구하기
    //no_seen.find(name)는 name이 no_seen 집합에 존재하면 그 위치의 반복자를 반환하고, 존재하지 않으면 no_seen.end()를 반환합니다.
    vector<string> result;
    for (const auto& name : no_listened) {
        if (no_seen.find(name) != no_seen.end()) {
            result.push_back(name);
        }
    }

    // 사전 순으로 정렬
    sort(result.begin(), result.end());

    // 결과 출력
    cout << result.size() << endl;
    for (const auto& name : result) {
        cout << name << endl;
    }

    return 0;
}
