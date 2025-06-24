#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    priority_queue<int> max_heap; // 기본적으로 최대 힙으로 동작하는 priority_queue

    for (int i = 0; i < N; ++i) {
        int num;
        cin >> num;
        
        if (num == 0) {
            if (max_heap.empty()) {
                cout << "0" << endl;
            } else {
                cout << max_heap.top() << endl; // 최대값 출력
                max_heap.pop(); // 최대값 제거
            }
        } else {
            max_heap.push(num); // 새로운 값을 최대 힙에 추가
        }
    }
    
    return 0;
}
