from collections import deque
import sys
input = sys.stdin.readline

# 3차원 배열 BFS
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 3차원 배열 BFS
def bfs():
    while queue:
        x, y, z = queue.popleft()
        vis[z][x][y] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0 and vis[nz][nx][ny] == 0:
                queue.append((nx, ny, nz))
                graph[nz][nx][ny] = graph[z][x][y] + 1
                vis[nz][nx][ny] = 1

m, n, h = map(int, input().split())
graph = [[] for i in range(h)]
vis = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]
queue = deque()

isTrue = False
st = False

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append((x, y, z))
bfs()
max_num = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num, graph[z][x][y])
if isTrue == True:
    print(-1)
else:
    print(max_num - 1)