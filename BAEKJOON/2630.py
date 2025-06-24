import sys
input = sys.stdin.readline

def colored_paper(size, x, y, paper):
    color = paper[x][y] #컬러하나를 지정 그게 검정색이던 하양색이던
    all_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                all_same = False
                break
        if not all_same:
            break

    if all_same: #만약 모두 같다면
        if color == 0:
            return (1, 0)  # 흰색 반환
        else:
            return (0, 1)  # 검은색 반환
    else: #다르다면
        half = size // 2 #크기를 줄이고 재귀하는 방법으로 다시 구해서 white,blxxqack의 개수를 구함
        white1, black1 = colored_paper(half, x, y, paper)
        white2, black2 = colored_paper(half, x, y + half, paper)
        white3, black3 = colored_paper(half, x + half, y, paper)
        white4, black4 = colored_paper(half, x + half, y + half, paper)
        return (white1 + white2 + white3 + white4, black1 + black2 + black3 + black4)

N = int(input().strip())
paper = [list(map(int, input().strip().split())) for _ in range(N)]

white, black = colored_paper(N, 0, 0, paper)
print(white)
print(black)
