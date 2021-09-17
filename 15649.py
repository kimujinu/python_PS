# Backtracking
def dfs(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    for i in range(1,N+1):
        if vis[i] == 0:
            graph[n] = i
            vis[i] = 1
            dfs(n + 1)
            vis[i] = 0

N,M = map(int,input().split())
graph = [0] * 10
vis = [0] * 10
dfs(0)