# 문제 : 두 동전
# N×M 크기의 보드와 4개의 버튼으로 이루어진 게임이 있다. 보드는 1×1크기의 정사각형 칸으로 나누어져 있고, 각각의 칸은 비어있거나, 벽이다.
# 두 개의 빈 칸에는 동전이 하나씩 놓여져 있고, 두 동전의 위치는 다르다.
# 버튼은 "왼쪽", "오른쪽", "위", "아래"와 같이 4가지가 있다. 버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 동시에 이동하게 된다.
# 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
# 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
# 그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
# 두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
import sys
from collections import deque

N,M = map(int,input().split())
graph = []
temp = []
count = 0
coin = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    graph.append(sys.stdin.readline().rstrip())

def bfs():
    global result
    while coin:
        x1,y1,x2,y2,cnt = coin.popleft()
        if cnt >= 10 :
            return -1
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0<=nx1<N and 0<=ny1<M and 0<=nx2<N and 0<=ny2<M:
                if graph[nx1][ny1] == "#":
                    nx1,ny1 = x1,y1
                if graph[nx2][ny2] == "#":
                    nx2,ny2 = x2,y2
                coin.append((nx1,ny1,nx2,ny2,cnt+1))
            elif 0<=nx1<N and 0<=ny1<M:
                return cnt + 1
            elif 0<=nx2<N and 0<=ny2<M:
                return cnt + 1
            else:
                continue
    return -1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'o':
            temp.append((i,j))

coin.append((temp[0][0],temp[0][1],temp[1][0],temp[1][1],0))

print(bfs())
