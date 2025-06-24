#include <iostream>
#include <vector>
#include <string>
#include <algorithm> 
using namespace std;

int N,M;

int main() {
    cin >> N >> M;
    
    vector<int> trees(N);

    int tree,result;
    

    result=0;

    for (int i = 0; i < N; i++) {
        cin >> trees[i];
    }

    sort(trees.begin(), trees.end());
    int start = 0;
    int end = trees.back();

    while (start <= end) {
        int mid = (start + end)/2;
        long long total = 0;
        for (int i= 0; i<N; i ++){
            if (trees[i] > mid){
                total+=trees[i]-mid;
            }
        }

        if (total >= M){
            result = mid;
            start = mid +1;
        }
        else
            end = mid -1;
    }

    cout << result;
}