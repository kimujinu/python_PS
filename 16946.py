# 문제 : 벽 부수고 이동하기 4(flood-fill)
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고,
# 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 한 칸에서 다른 칸으로 이동하려면,
# 두 칸이 인접해야 한다. 두 칸이 변을 공유할 때, 인접하다고 한다.
# 각각의 벽에 대해서 다음을 구해보려고 한다.
# 벽을 부수고 이동할 수 있는 곳으로 변경한다.
# 그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다.
# 출력
# 맵의 형태로 정답을 출력한다. 원래 빈 칸인 곳은 0을 출력하고,
# 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력한다.
# 0인 곳을 큐에 넣어서 주변 1인곳에 값을 퍼트려준다.(Flood-fill)
import sys
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int,sys.stdin.readline().split())
graph = []
graph2 = [[0]*M for _ in range(N)]
vis = [[0]*M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph2[i][j] = 1

def bfs(x,y):
    global values
    queue = deque()
    queue.append((x,y))
    vis[x][y] = 1
    temp2 = []
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if vis[nx][ny] == 0:
                    vis[nx][ny] = 1
                    if graph[nx][ny] == 0:
                        queue.append((nx,ny))
                        values += 1
                    else:
                        temp2.append((nx,ny))
    for x,y in temp2:
        vis[x][y] = 0
        graph2[x][y] += values
        if graph2[x][y]>=10:graph2[x][y] %=10

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and vis[i][j] == 0:
            values = 1
            bfs(i,j)

for i in range(N):
    for j in range(M):
        print(graph2[i][j],end='')
    print()


