# 문제 : 치즈
# 아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고,
# 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다.
# 판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.
# 이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다.
# 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다.
# <그림 1>의 경우, 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어져서 <그림 2>와 같이 된다.
# <그림 3>은 원래 치즈의 두 시간 후 모양을 나타내고 있으며,
# 남은 조각들은 한 시간이 더 지나면 모두 녹아 없어진다.
# 그러므로 처음 치즈가 모두 녹아 없어지는 데는 세 시간이 걸린다.
# <그림 3>과 같이 치즈가 녹는 과정에서 여러 조각으로 나누어 질 수도 있다.
# 입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때,
# 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다.
# 세로와 가로의 길이는 최대 100이다.
# 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다.
# 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.
# 출력
# 첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고,
# 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.
import sys
from collections import deque

H,W = map(int,sys.stdin.readline().split())
graph = []
count = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(H):
    graph.append(list(map(int,sys.stdin.readline().split())))

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<H and 0<=ny<W:
                if graph[nx][ny] == 0 and vis[nx][ny] == 0:
                    queue.append((nx,ny))
                    vis[nx][ny] = 1
                elif graph[nx][ny] == 1 and vis[nx][ny] == 0:
                    temp_delete.append((nx,ny))
                    vis[nx][ny] = 1

def check(result):
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                result += 1
    return result

while True:
    temp_delete = []
    vis = [[0]*W for _ in range(H)]
    queue = deque()
    result = 0
    result = check(0)
    if result == 0: # 1이 없을 때
        print(result)
        print(count)
        break
    count += 1
    for i in range(H):
        if i == 0 or i == H-1:
            for j in range(W):
                vis[i][j] = 1
                queue.append((i,j))
        else:
            for j in (i,0),(i,W-1):
                vis[j[0]][j[1]] = 1
                queue.append(j)
    bfs()

    for x,y in temp_delete:
        graph[x][y] = 0

    temp_result = check(0)
    if temp_result == 0:
        print(count)
        print(result)
        break










