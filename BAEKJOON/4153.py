def check(lines):
    for line in lines:
        if line!=0:
            return -1
    return 1

while(True):
    lines=list(map(int,input().split()))
    if (check(lines)==1):
        break
    max_line=max(lines)
    del lines[lines.index(max_line)]
    if lines[0]*lines[0]+lines[1]*lines[1]==max_line*max_line:
        print("right")
    else:
        print("wrong")
        
# gpt 코드

# def is_right_triangle(sides):
#     # 정렬하여 가장 긴 변을 마지막으로 오게 한다.
#     sides = sorted(sides)
#     # 피타고라스의 정리를 사용하여 직각 삼각형인지 확인
#     if sides[0]**2 + sides[1]**2 == sides[2]**2:
#         return "right"
#     else:
#         return "wrong"

# while True:
#     sides = list(map(int, input().strip().split()))
#     if sides == [0, 0, 0]:
#         break
#     print(is_right_triangle(sides))
