import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> rank = new HashMap<>();
        
        for (int i=0; i < players.length; i++) {
            rank.put( players[i] , i);
        }
        
        for (String name : callings){
            int k = rank.get(name);
            
            String frontPlayer = players[k-1];
            players[k]=frontPlayer;
            players[k-1]=name;
            
            rank.put(frontPlayer,k);
            rank.put(name,k-1);
        }
        
        return players;
    }
}