from collections import deque
import sys

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])
    vis[x][y][z] = 1
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if graph[nx][ny][nz] == 'E':
                    print("Escaped in {0} minute(s).".format(vis[x][y][z]))
                    return
                if graph[nx][ny][nz] == '.' and vis[nx][ny][nz] == 0:
                    vis[nx][ny][nz] = vis[x][y][z] + 1
                    queue.append([nx, ny, nz])
    print("Trapped!")

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    graph = [[[]*C for _ in range(R)] for _ in range(L)]
    vis = [[[0]*C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        graph[i] = [list(sys.stdin.readline().strip()) for _ in range(R)]
        input()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    bfs(i, j, k)