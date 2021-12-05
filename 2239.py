# 문제 : 스도쿠
# 스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때,
# 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
# 예를 들어 다음을 보자.
# 위 그림은 참 잘도 스도쿠 퍼즐을 푼 경우이다.
# 각 행에 1부터 9까지의 숫자가 중복 없이 나오고,
# 각 열에 1부터 9까지의 숫자가 중복 없이 나오고,
# 각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
# 하다 만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내는 프로그램을 작성하시오.

sdoku = []
zero = []
for _ in range(9):
    sdoku.append(list(map(int,input().rstrip())))

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zero.append((i,j))

def col_check(y,value):
    for i in range(9):
        if sdoku[i][y] == value:
            return False
    return True

def row_check(x,value):
    for i in range(9):
        if sdoku[x][i] == value:
            return False
    return True


def sq_check(x,y,value):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if sdoku[nx+i][ny+j] == value:
                return False
    return True

def solve(level):
    if level == len(zero):
        for i in range(9):
            for j in range(9):
                print(sdoku[i][j],end='')
            print()
        exit(0)
    for i in range(1,10):
        nx = zero[level][0]
        ny = zero[level][1]
        if col_check(ny,i) and row_check(nx,i) and sq_check(nx,ny,i):
            sdoku[nx][ny] = i
            solve(level+1)
            sdoku[nx][ny] = 0

solve(0)