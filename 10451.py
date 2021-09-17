
def dfs(v,i):
    global count
    vis[v] = True
    for j in graph[v]:
        if not vis[j]:
            dfs(j,i)
        elif vis[j] and j==i:
            count += 1



T = int(input())
for i in range(T):
    count = 0
    N = int(input())
    graph = [[] for _ in range(N+1)]
    temp = list(map(int,input().split()))
    vis = [False] * (N + 1)
    for j in range(len(temp)):
        graph[j+1].append(temp[j])
    for j in range(N+1):
        dfs(j,j)
    print(count)