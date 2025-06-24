#include <iostream>
#include <string>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;  // N과 M 입력

    string S;
    cin >> S;  // 문자열 S 입력

    // 패턴 "IOI"를 반복해서 P 패턴 생성
    string P = "I";
    for (int i = 0; i < N; i++) {
        P += "OI";
    }

    int count = 0;  // 패턴이 발견된 횟수를 셀 변수

    // S 문자열에서 P 패턴을 찾기 위한 루프
    for (int i = 0; i <= M - P.size(); i++) {
        if (S.substr(i, P.size()) == P) {  // 현재 위치에서 P 패턴과 일치하는지 확인
            count++;  // 패턴이 일치하면 count 증가
        }
    }

    cout << count << endl;  // 결과 출력

    return 0;
}
