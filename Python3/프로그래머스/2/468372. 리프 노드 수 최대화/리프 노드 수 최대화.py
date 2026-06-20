def solution(dist_limit, split_limit):
    answer = [0]
    
    def dfs(cur, used, split, leaf):
        # cur: 현재 레벨에서 분배노드로 쓸 수 있는 노드 수
        # used: 지금까지 사용한 분배노드 수
        # split: 현재까지의 분배도 (곱)
        # leaf: 지금까지 확정된 리프 노드 수
        
        # cur개의 노드가 더 내려가지 못하면 전부 리프가 됨
        answer[0] = max(answer[0], leaf + cur)
        
        for child in [2, 3]:
            # 분배도 초과하면 이 분기 포기
            if split * child > split_limit or used > dist_limit:
                continue
            
            # 현재 cur개 노드가 child배로 분기 → 다음 레벨 노드 수 현재 // 레벨에서 쓸 수 있는 분배노드 * 자식수
            next_nodes = cur * child
            
            # 남은 분배노드 슬롯 
            remain = dist_limit - used
            
            # 다음 레벨 노드 중 실제로 분배노드가 될 수 있는 수
            # (남은 슬롯보다 많으면 슬롯만큼만)
            next_cur = min(next_nodes, remain)
            
            # 분배노드가 못된 나머지는 리프로 확정
            next_leaf = leaf + (next_nodes - next_cur)
            
            dfs(
                next_cur,           # 다음 레벨 분배노드 수
                used + next_cur,    # 누적 사용량 갱신
                split * child,      # 분배도 갱신
                next_leaf           # 누적 리프 수
            )
    
    # 루트의 자식(깊이1) 1개에서 시작, 분배노드 1개 사용
    dfs(1, 1, 1, 0)
    return answer[0]