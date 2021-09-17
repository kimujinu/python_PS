from collections import deque

def bfs(x,y):
    a = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < M and graph[nx][ny] != 0 :
                queue.append((nx,ny))
                graph[nx][ny] = 0
                a += 1
    return a

dx = [-1,1,0,0]
dy = [0,0,-1,1]

M,N,K = map(int,input().split())
graph = [[1]*M for _ in range(N)]

for _ in range(K):
    l_x,l_y,r_x,r_y = map(int, input().split())
    for i in range(l_x,r_x):
        for j in range(l_y,r_y):
            graph[i][j] = 0

count = 0
result = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 :
            count += 1
            result.append(bfs(i,j))

print(count)
result.sort()
for i in result:
    print(i,end=' ')

