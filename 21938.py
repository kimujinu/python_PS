# 문제 : 영상처리
# 간단하지만 귀찮은 영상처리 과제가 주어졌다. 과제의 명세는 다음과 같다.
# 세로 길이가 $N$이고 가로 길이가 $M$인 화면은 총 $N$ × $M$개의 픽셀로 구성되어 있고 $(i, j)$에 있는 픽셀은 $R_{i,j}$ (Red), $G_{i,j}$ (Green), $B_{i,j}$ (Blue) 3가지 색상의 의미를 담고 있다.
# 각 색상은 0이상 255이하인 값으로 표현 가능하다.
# 모든 픽셀에서 세 가지 색상을 평균내어 경계값 $T$보다 크거나 같으면 픽셀의 값을 255로, 작으면 0으로 바꿔서 새로운 화면으로 저장한다.
# 새로 만들어진 화면에서 값이 255인 픽셀은 물체로 인식한다. 값이 255인 픽셀들이 상하좌우로 인접해있다면 이 픽셀들은 같은 물체로 인식된다.
# 화면에서 물체가 총 몇 개 있는지 구하는 프로그램을 작성하시오.
from collections import deque

def bfs(x,y):
    global vis,result
    queue = deque()
    queue.append((x,y))
    vis[x][y] = 1
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if vis[nx][ny]==0 and graph[nx][ny] == 255:
                    vis[nx][ny] = 1
                    queue.append((nx,ny))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
vis = [[0]*M for _ in range(N)]
temp = []
total = 0
for i in range(1,N+1):
    temp.append(list(map(int,input().split())))
T = int(input())
for i in range(N):
    for j in range(1,(M*3)+1):
        if j%3 == 0:
            total+=temp[i][j-1]
            temp1 = 0
            if total//3 >= T :
                temp1 = 255
            else:
                temp1 = 0
            graph[i].append(temp1)
            total = 0
        else:
            total += temp[i][j-1]


result = 0
queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 255 and vis[i][j] == 0:
            bfs(i,j)
            result+=1

print(result)


