#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <tuple>

using namespace std;

int D(int n) {
    return (2 * n) % 10000;
}

int S(int n) {
    return (n == 0) ? 9999 : n - 1; //if n==0 이면 9999 else : n-1
}

int L(int n) {
    return (n % 1000) * 10 + n / 1000;
}

int R(int n) {
    return (n % 10) * 1000 + n / 10;
}

string bfs(int A, int B) {
    queue<pair<int, string>> q;
    vector<bool> visited(10000, false);
    
    q.push({A, ""});
    visited[A] = true;
    
    while (!q.empty()) {
        int current;
        string operations;
        tie(current, operations) = q.front();
        q.pop();
        
        if (current == B) {
            return operations;
        }
        
        // D operation
        int next_num = D(current);
        if (!visited[next_num]) {
            visited[next_num] = true;
            q.push({next_num, operations + "D"});
        }
        
        // S operation
        next_num = S(current);
        if (!visited[next_num]) {
            visited[next_num] = true;
            q.push({next_num, operations + "S"});
        }
        
        // L operation
        next_num = L(current);
        if (!visited[next_num]) {
            visited[next_num] = true;
            q.push({next_num, operations + "L"});
        }
        
        // R operation
        next_num = R(current);
        if (!visited[next_num]) {
            visited[next_num] = true;
            q.push({next_num, operations + "R"});
        }
    }
    
    return "";
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int A, B;
        cin >> A >> B;
        cout << bfs(A, B) << endl;
    }

    return 0;
}
