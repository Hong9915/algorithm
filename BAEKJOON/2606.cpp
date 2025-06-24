#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

// BFS를 통해 바이러스가 퍼지는 컴퓨터를 추적하는 함수
set<int> virus(int start, const vector<vector<int>>& graph) {
    set<int> visited; // 감염된 컴퓨터를 추적하기 위한 집합
    queue<int> q;     // BFS를 위한 큐
    q.push(start);

    while (!q.empty()) {
        int i = q.front();
        q.pop();

        if (visited.find(i) == visited.end()) {
            visited.insert(i);
            for (int neighbor : graph[i]) {
                if (visited.find(neighbor) == visited.end()) {
                    q.push(neighbor);
                }
            }
        }
    }

    return visited;
}

int main() {
    int N, M;
    cin >> N >> M;

    // 그래프 초기화 (1번 컴퓨터부터 N번 컴퓨터까지)
    vector<vector<int>> graph(N + 1);

    // 네트워크 연결 정보 입력
    for (int i = 0; i < M; i++) {
        int key, value;
        cin >> key >> value;
        graph[key].push_back(value);
        graph[value].push_back(key);
    }

    // 1번 컴퓨터에서 바이러스 확산
    set<int> infected = virus(1, graph);

    // 1번 컴퓨터를 제외한 감염된 컴퓨터 수 출력
    cout << infected.size() - 1 << endl;

    return 0;
}
