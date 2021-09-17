from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0<= ny < M and graph[nx][ny]==1:
                graph[nx][ny] = 0
                queue.append((nx,ny))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())

for _ in range(T):
    a = 0
    M,N,K = map(int,input().split())

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
                a+=1

    print(a)