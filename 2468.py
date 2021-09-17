from copy import deepcopy
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    vis[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and vis[nx][ny] > k:
                queue.append((nx,ny))
                vis[nx][ny] = 1
    return 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 1
for k in range(1, max(map(max, graph))+1): #각 높이에서 최대 영역구하기
    vis = deepcopy(graph)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if vis[i][j] > k:
                vis[i][j] = k
                bfs(i, j)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)