
def backTracking(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    st = 1
    if n != 0 :
        st = graph[n-1] + 1
    for i in range(st,N+1):
        if vis[i] == 0:
            vis[i] = 1
            graph[n] = i
            backTracking(n+1)
            vis[i] = 0

N,M = map(int,input().split())
graph = [0] * 10
vis = [0] * 10
backTracking(0)