#include <iostream>    // 표준 입출력을 위한 헤더 파일
#include <deque>       // deque 컨테이너를 사용하기 위한 헤더 파일
#include <string>      // 문자열 처리를 위한 헤더 파일
#include <sstream>     // 문자열 스트림을 사용하기 위한 헤더 파일
using namespace std;

int main() {
    int T;
    cin >> T;  // 테스트 케이스의 수 입력

    while (T--) {  // T가 0이 될 때까지 반복 (T를 1씩 감소시키면서)
        string p;
        cin >> p;  // 명령어 문자열 입력 (예: "RDD")

        int n;
        cin >> n;  // 배열의 길이 입력

        string arr_str;
        cin >> arr_str;  // 배열을 문자열로 입력 (예: "[1,2,3,4]")

        // 대괄호 제거 후 ','로 나눠서 숫자들을 deque에 넣기
        deque<int> number_list;
        stringstream ss(arr_str.substr(1, arr_str.size() - 2)); // 양 끝 대괄호 제거 후 문자열 스트림으로 변환
        string item;
        while (getline(ss, item, ',')) {  // 쉼표를 기준으로 문자열을 잘라서 숫자 추출
            if (!item.empty()) {  // 비어 있지 않은 경우에만
                number_list.push_back(stoi(item));  // 숫자로 변환하여 deque에 추가
            }
        }

        bool reversed_flag = false;  // 리스트가 뒤집힌 상태인지 추적하는 플래그
        bool error_flag = false;  // 에러가 발생했는지 추적하는 플래그

        for (char cmd : p) {  // 명령어 문자열의 각 문자를 순회
            if (cmd == 'R') {  // 'R' 명령어인 경우
                reversed_flag = !reversed_flag;  // 뒤집힌 상태를 반전시킴 (True -> False, False -> True)
            } else if (cmd == 'D') {  // 'D' 명령어인 경우
                if (number_list.empty()) {  // deque가 비어 있으면
                    cout << "error" << endl;  // "error" 출력
                    error_flag = true;  // 에러 플래그 설정
                    break;  // 명령어 처리 중단
                }
                if (reversed_flag) {  // 뒤집힌 상태이면
                    number_list.pop_back();  // 뒤에서 요소 제거
                } else {  // 뒤집히지 않은 상태이면
                    number_list.pop_front();  // 앞에서 요소 제거
                }
            }
        }

        if (!error_flag) {  // 에러가 발생하지 않았을 경우에만 결과 출력
            cout << "[";
            while (!number_list.empty()) {  // deque가 비어있지 않은 동안
                if (reversed_flag) {  // 뒤집힌 상태라면
                    cout << number_list.back();  // 뒤쪽 요소 출력
                    number_list.pop_back();  // 뒤쪽 요소 제거
                } else {  // 뒤집히지 않은 상태라면
                    cout << number_list.front();  // 앞쪽 요소 출력
                    number_list.pop_front();  // 앞쪽 요소 제거
                }
                if (!number_list.empty()) {  // 아직 출력할 요소가 남아 있다면
                    cout << ",";  // 쉼표 출력
                }
            }
            cout << "]" << endl;  // 닫는 대괄호와 줄바꿈 출력
        }
    }

    return 0;  // 프로그램 종료
}
