# 문제 : 미세먼지 안녕!(SAMSUNG)
# 미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다.
# 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다.
# 공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.
# 1초 동안 아래 적힌 일이 순서대로 일어난다.
# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
# 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
# 다음은 확산의 예시이다.
# 왼쪽과 오른쪽에 칸이 없기 때문에, 두 방향으로만 확산이 일어났다.
# 인접한 네 방향으로 모두 확산이 일어난다.
# 공기청정기가 있는 칸으로는 확산이 일어나지 않는다.
# 공기청정기의 바람은 다음과 같은 방향으로 순환한다.
# 방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.
# 입력
# 첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
# 둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다.
# 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다.
# -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
# 출력
# 첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def spread(x, y):	# 먼지 증식
    cnt = board[x][y]	# 현재 먼지의 수
    for d in range(4):	# 상하좌우
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < R and 0 <= Y < C:	# 위치가 board 안인지 체크
            if board[X][Y] >= 0:	# 위치에 청소기가 없다면
                sub_board[X][Y] += board[x][y]//5	# 새로운 board에 먼지 증식
                cnt -= board[x][y]//5	# 증식한 만큼 빼기
    sub_board[x][y] += cnt	# 새로운 board에 증식한 먼지를 제외한 만큼 넣기

def cleanup(x):	# 청소기 윗부분 처리
    dx = [0, -1, 0, 1]		# 청소 진행방향 우, 상, 좌, 하
    dy = [1, 0, -1, 0]

    now = sub_board[x][1]	# 첫번째 청소할 구역의 먼지 기록
    sub_board[x][1] = 0		# 첫번째 구역 청소
    d = 0	# 방향
    X = x
    Y = 1
    while True:
        X += dx[d]
        Y += dy[d]
        next = sub_board[X][Y]	# 청소 예정 구역의 먼지 기록
        sub_board[X][Y] = now	# 청소 (앞에서 가져온 먼지 저장)
        now = next	# next에서 기록한 먼지를 다음에 쓰기 위해 now로 옮김
        if X + dx[d] < 0 or X + dx[d] > x or Y + dy[d] < 0 or Y + dy[d] >= C:	# 방향을 바꿔야할 때
            d += 1
        if d == 4:	# 모든 방향을 청소했을 때
            break

def cleandown(x):	# 청소기 아랫부분 처리
    dx = [0, 1, 0, -1]	# 청소 진행방향 우, 하, 좌, 상
    dy = [1, 0, -1, 0]
								# cleanup 함수와 동일. (방향 바꾸기 처리만 다름)
    now = sub_board[x][1]
    sub_board[x][1] = 0
    d = 0
    X = x
    Y = 1
    while True:
        X += dx[d]
        Y += dy[d]
        next = sub_board[X][Y]
        sub_board[X][Y] = now
        now = next
        if X + dx[d] < x or X + dx[d] >= R or Y + dy[d] < 0 or Y + dy[d] >= C:
            d += 1
        if d == 4:
            break

R, C, T = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))

v1 = 0	# 청소기 윗부분
v2 = 1	# 청소기 아랫부분

for i in range(R):
    if board[i][0] == -1:	# 청소기 위치찾기
        v1 = i
        v2 = i+1
        break

for _ in range(T):  # 몇회 반복
    sub_board = [[0]*C for __ in range(R)]	# 결과를 임시기록할 board

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:	# 먼지가 있으면
                spread(i, j)	# 먼지 증식
    cleanup(v1)
    cleandown(v2)
    sub_board[v1][0] = -1		# 청소기 위치에 청소기 저장
    sub_board[v2][0] = -1
    board = sub_board		# 임시기록한 board를 진짜 board에 옮김

answer = 0
for i in range(R):
    for j in range(C):
        answer += board[i][j]
print(answer+2)