# 문제 : 전구를 켜라 (0-1 너비우선탐색)
# 선영이는 N × M 직사각형 크기의 전자 회로를 디자인 하고 있다. 회로에는 N × M개의 정사각형 타일이 있고, 모두 직사각형의 변과 평행하다. 모든 타일은 두 개의 마주보는 꼭짓점이 전선으로 연결되어 있다. (그림 참조)
#
# 전원은 왼쪽 위 모서리에 연결되어 있고, 전구는 오른쪽 아래 모서리에 연결되어 있다. 전구는  전원에서 전구로 가는 경로가 있을 때만 불이 켜진다. 전구에 불을 켜기 위해서, 선영이는 몇개의 타일을 90도 회전 시킬 수 있다.
# 위의 그림에서 전구는 꺼져있다. 만약 오른쪽에서 2번째 열 중 아무 칸이나 90도 회전시킨다면, 전원과 전구는 연결되어 전구가 켜지게 된다. 전구에 불을 켜기 위해 돌려야 하는 칸의 개수의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 M이 주어진다. 둘째 줄부터 N개의 줄에는 전자 회로의 상태가 주어진다. 상태는 / 또는 \이다. (1 ≤ N, M ≤ 500)
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다. 전구에 불을 켜는 것이 가능하면, 몇 개의 칸을 돌려야 하는지를 출력하고, 불가능할때는 "NO SOLUTION"을 따옴표 없이 출력한다.
import sys
from collections import deque

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

N,M = map(int,sys.stdin.readline().split())
graph = []
vis = [[0]*M for _ in range(N)]
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
def check(dir):
    if dir == '\\':
        return '/'
    else:
        return '\\'

def bfs():
    queue = deque()
    if graph[0][0] == '\\':
        queue.append((0,0,0,'\\'))
    else:
        queue.append((0,0,1,'\\'))
    vis[0][0] = 1
    while queue:
        x,y,c,h = queue.popleft()
        if x == N-1 and y == M-1:
            if h == '\\':
                return c
            else:
                return "NO SOLUTION"
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and vis[nx][ny] == 0:
                if i<4:
                    vis[nx][ny] = 1
                    if graph[nx][ny] != h:
                        queue.appendleft((nx,ny,c,check(h))) # 빠르게 갈수 있는 방향일때 먼저 삽입
                    else:
                        queue.append((nx,ny,c+1,check(h)))
                elif i == 4 or i == 5:
                    if h == '\\':
                        if graph[nx][ny] == '\\':
                            vis[nx][ny] = 1
                            queue.appendleft((nx,ny,c,h)) # 빠르게 갈수 있는 방향일때 먼저 삽입
                        else:
                            vis[nx][ny] = 1
                            queue.append((nx,ny,c+1,h))
                else:
                    if h == '/':
                        if graph[nx][ny] == '/':
                            vis[nx][ny] = 1
                            queue.appendleft((nx,ny,c,h)) # 빠르게 갈수 있는 방향일때 먼저 삽입
                        else:
                            vis[nx][ny] = 1
                            queue.append((nx,ny,c+1,h))
print(bfs())
