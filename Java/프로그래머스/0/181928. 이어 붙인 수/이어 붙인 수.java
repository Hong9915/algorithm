class Solution {
    public int solution(int[] num_list) {
        StringBuilder oddBuilder = new StringBuilder();
        StringBuilder evenBuilder = new StringBuilder();

        for (int num : num_list) {
            if (num % 2 == 0) { 
                evenBuilder.append(num);
            } else { 
                oddBuilder.append(num);
            }
        }

        int oddNum = Integer.parseInt(oddBuilder.toString());
        int evenNum = Integer.parseInt(evenBuilder.toString());

        return oddNum + evenNum;
    }
}