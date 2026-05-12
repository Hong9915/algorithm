import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int j = 0;
        for (int i=0; i<enemy.length; i++){
            pq.add(-enemy[i]);
            n = n - enemy[i];
            if (n < 0){
                if(k==0){
                    return i;
                }
                
                n = n - pq.poll();
                k = k - 1;
            }
        }
        return enemy.length;
    }
}