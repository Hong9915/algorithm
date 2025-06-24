#이걸 어케하냐 ㅅㅂ
def draw_star(n):
  if n == 3:
      # 기본 삼각형 반환
      return ["  *  ", " * * ", "*****"]
  
  # 이전 단계 삼각형
  prev = draw_star(n // 2)
  space = " " * (n // 2)
  
  # 새로운 삼각형 구성
  result = []
#   for line in prev:
#       print(line)
  for line in prev:
      result.append(space + line + space)  # 위쪽 삼각형
  for line in prev:
      result.append(line + " " + line)

  return result

# 입력 처리
n = int(input().strip())  # N 입력
star = draw_star(n)

# 출력
for line in star:
  print(line)