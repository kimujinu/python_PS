from collections import deque

def dfs(v):
    vis[v] = 1
    print(v,end=' ')
    for i in range(1,N+1):
        if vis[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    vis2[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        nx = queue.popleft()
        print(nx,end=' ')
        for i in range(1,N+1):
            if vis2[i]==0 and graph[nx][i] == 1:
                queue.append(i)
                vis2[i] = 1


N,M,V = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
vis = [0] * (N+1)
vis2 = [0] * (N+1)

for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

dfs(V)
print()
bfs(V)