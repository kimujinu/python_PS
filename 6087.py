# 문제 : 레이저 통신 (0-1 너비우선탐색)
# 크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.
#
# 'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.
#
# 레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다.
#
# 아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.
#
# 7 . . . . . . .         7 . . . . . . .
# 6 . . . . . . C         6 . . . . . /-C
# 5 . . . . . . *         5 . . . . . | *
# 4 * * * * * . *         4 * * * * * | *
# 3 . . . . * . .         3 . . . . * | .
# 2 . . . . * . .         2 . . . . * | .
# 1 . C . . * . .         1 . C . . * | .
# 0 . . . . . . .         0 . \-------/ .
#   0 1 2 3 4 5 6           0 1 2 3 4 5 6
# 입력
# 첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)
#
# 둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.
#
# .: 빈 칸
# *: 벽
# C: 레이저로 연결해야 하는 칸
# 'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.
#
# 출력
# 첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.
from collections import deque
import sys
W,H = map(int,sys.stdin.readline().split())
graph = []
C_list = []
vis = [[0]*W for _ in range(H)]
for _ in range(H):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(st_a,st_b):
    queue = deque()
    queue.append((st_a,st_b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0<=nx<H and 0<=ny<W and graph[nx][ny] != '*':
                if vis[nx][ny] == 0:
                    vis[nx][ny] = vis[x][y] + 1
                    queue.append((nx,ny))
                nx = nx + dx[i]
                ny = ny + dy[i]

for i in range(H):
    for j in range(W):
        if graph[i][j] == 'C':
           C_list.append((i,j))

(start_a,start_b),(end_a,end_b) = C_list

bfs(start_a,start_b)
print(vis[end_a][end_b]-1)
