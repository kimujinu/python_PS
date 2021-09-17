from collections import deque
import sys

# 응용 3 - 시작점이 두 종류 일때
# 불이 지나간 자리에 
def bfs() :

    while fire_q:
        x,y = fire_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C :
               if f_vis[nx][ny] == 0 and graph[nx][ny] != '#':
                    f_vis[nx][ny] = f_vis[x][y] + 1
                    fire_q.append((nx,ny))

    while j_q:
        x,y = j_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C :
                return j_vis2[x][y] + 1

            if j_vis2[nx][ny] != 0 or graph[nx][ny] == '#' or (f_vis[nx][ny] != 0 and f_vis[nx][ny] <= j_vis2[x][y]+1):
                continue

            j_vis2[nx][ny] = j_vis2[x][y] + 1
            j_q.append((nx,ny))

    return "IMPOSSIBLE"


# 시작점이 두 종류 일때
R,C = map(int,sys.stdin.readline().split())

j_q = deque()
fire_q = deque()

f_vis = [[0] * C for _ in range(R)]
j_vis2 = [[0] * C for _ in range(R)]
graph = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            fire_q.append((i,j))
        if graph[i][j] == 'J':
            j_q.append((i,j))

print(bfs())

