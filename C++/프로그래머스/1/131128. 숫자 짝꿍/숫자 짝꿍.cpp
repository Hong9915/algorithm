#include <string>
#include <vector>

using namespace std;

string solution(string X, string Y) {
    string answer = "";
    int countX[10] = {0};
    int countY[10] = {0};
    
    for (int i = 0; i < X.size(); i++) countX[X[i] - '0']++;
    for (int i = 0; i < Y.size(); i++) countY[Y[i] - '0']++;
    
    for (int i = 9; i>=0; i--){
        int common = min(countX[i],countY[i]);
        for (int j = 0; j < common; j ++){
            answer += to_string(i) ;
        }
    }
    if (answer.empty()) return "-1";
    if (answer[0] == '0') return "0";
    return answer;
}