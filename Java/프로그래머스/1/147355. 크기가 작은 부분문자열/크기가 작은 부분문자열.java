public class Solution {
    public int solution(String t, String p) {
        int count = 0;
        int len = p.length();
        long pNum = Long.parseLong(p); // p를 숫자로 변환

        for (int i = 0; i <= t.length() - len; i++) {
            String sub = t.substring(i, i + len); // 부분 문자열 추출
            long subNum = Long.parseLong(sub);   // 숫자로 변환

            if (subNum <= pNum) {
                count++;
            }
        }

        return count;
    }
}