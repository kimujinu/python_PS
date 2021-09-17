from collections import deque
import sys

def bfs():
    while fire_q:
        x,y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if f_vis[nx][ny] == 0 and graph[nx][ny] != '#':
                    fire_q.append((nx,ny))
                    f_vis[nx][ny] = f_vis[x][y]+1

    while j_q:
        x,y = j_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w :
                return j_vis2[x][y]

            if j_vis2[nx][ny] != 0 or graph[nx][ny] == '#' or (f_vis[nx][ny] != 0 and f_vis[nx][ny] <= j_vis2[x][y] + 1):
                continue

            j_q.append((nx,ny))
            j_vis2[nx][ny] = j_vis2[x][y] + 1

    return "IMPOSSIBLE"

dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for _ in range(T):
    j_q = deque()
    fire_q = deque()
    w,h = map(int,input().split())
    f_vis = [[0] * w for _ in range(h)]
    j_vis2 = [[0] * w for _ in range(h)]
    graph = [list(sys.stdin.readline().strip()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                fire_q.append((i,j))
                f_vis[i][j] = 1
            if graph[i][j] == '@':
                j_q.append((i,j))
                j_vis2[i][j] = 1

    print(bfs())