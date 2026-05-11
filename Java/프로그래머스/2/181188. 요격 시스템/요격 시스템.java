import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        Arrays.sort(targets,(a,b) -> a[1] -b[1]);
        double line = -100000000;
        int answer = 0;
        
        
         for (int[] target : targets) {

            if (line < target[0]){
                line = target[1]-0.1;
                answer+=1;
            }

        }
        return answer;
    }
}