

def bfs(x,y):
    return

N,M = map(int,input().split())
graph = [[0] * M] * N
for i in range(N):
    graph[i] = list(map(int,input().split()))

for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and graph[i][j] != 6:
            bfs(i,j)