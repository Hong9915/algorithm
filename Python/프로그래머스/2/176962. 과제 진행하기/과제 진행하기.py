from collections import deque

def solution(plans):
    answer = []

    def time_to_minutes(time):
        hour, minutes = map(int, time.split(":"))
        return hour * 60 + minutes

    for plan in plans:
        plan[1] = time_to_minutes(plan[1])
        plan[2] = int(plan[2])

    plans.sort(key=lambda x: x[1])

    queue = deque()
    time = plans[0][1]
    queue.append((plans[0][0], plans[0][2]))
    i = 1 

    while queue or i < len(plans):
        if i < len(plans) and not queue:
            queue.append((plans[i][0], plans[i][2]))
            time = plans[i][1]
            i += 1
            continue

        assignment, time_remained = queue.pop()

        if i < len(plans):
            next_start = plans[i][1]
            if time + time_remained > next_start:
                time_spent = next_start - time
                time += time_spent
                queue.append((assignment, time_remained - time_spent))
                queue.append((plans[i][0], plans[i][2]))
                i += 1
            else:
                time += time_remained
                answer.append(assignment)
        else:
            time += time_remained
            answer.append(assignment)

    return answer
