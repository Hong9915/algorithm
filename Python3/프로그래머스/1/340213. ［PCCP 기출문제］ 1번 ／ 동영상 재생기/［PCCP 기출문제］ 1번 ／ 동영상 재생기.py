def solution(video_len, pos, op_start, op_end, commands):
    def skip(t):
        if str_to_sec(op_start) <= t <= str_to_sec(op_end):
            return str_to_sec(op_end)
        return t

    def str_to_sec(s):
        mm, ss = map(int, s.split(":"))
        return mm * 60 + ss

    def sec_to_str(t):
        mm = t // 60
        ss = t % 60
        return f"{mm:02}:{ss:02}"

    cur_time = skip(str_to_sec(pos))

    for command in commands:
        if command == "next":
            cur_time += 10
            if cur_time > str_to_sec(video_len):
                cur_time = str_to_sec(video_len)
        elif command == "prev":
            cur_time -= 10
            if cur_time < 0:
                cur_time = 0
        cur_time = skip(cur_time)
 
    return sec_to_str(cur_time)
