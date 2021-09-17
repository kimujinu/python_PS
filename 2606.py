
def dfs(v):
    vis[v] = 1
    for i in range(1,M+1):
        if vis[i] == 0 and graph[v][i] == 1:
            dfs(i)

M = int(input())
N = int(input())
graph = [[0]*(M+1) for _ in range(M+1)]
vis = [0] * (M+1)
count = 0
for _ in range(N):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

dfs(1)
for i in vis:
    if i == 1:
        count += 1

print(count-1)