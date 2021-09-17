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

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 0 :
                queue.append((nx,ny))
                graph[nx][ny] = 0
                a += 1
    return a

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int,input())))

count = 0
result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 :
            result.append(bfs(i,j))
            count+=1

print(count)
result.sort()
for i in result:
    print(i)