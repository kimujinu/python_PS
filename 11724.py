
def dfs(v):
    vis[v] = 1
    for i in range(1,N+1):
        if vis[i] == 0 and graph[v][i] == 1:
            dfs(i)

N,M = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
vis = [0] * (N+1)
count = 0

for i in range(M):
    u,v = map(int,input().split())
    graph[u][v] = graph[v][u] = 1

for j in range(1,N+1):
    if not vis[j]:
        dfs(j)
        count += 1

print(count)