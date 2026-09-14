from collections import deque

def solution(n, infection, edges, k):
    answer = 0

    def spread(infected, pipe_type):
        new_infected = set(infected) 
        queue = deque(infected)       

        while queue:
            node = queue.popleft()
            for edge in edges:
                if edge[2] == pipe_type:
                    if edge[0] == node and edge[1] not in new_infected:
                        new_infected.add(edge[1])
                        queue.append(edge[1])
                    if edge[1] == node and edge[0] not in new_infected:
                        new_infected.add(edge[0])
                        queue.append(edge[0])

        return new_infected

    def dfs(infection_set, k):
        nonlocal answer
        answer = max(answer, len(infection_set))

        if k == 0:
            return

        for pipe_type in [1, 2, 3]:
            new_infected = spread(infection_set, pipe_type)
            if len(new_infected) > len(infection_set):  
                dfs(new_infected, k - 1)

    dfs({infection}, k)
    return answer