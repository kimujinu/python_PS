
def backtracking(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    st = 0
    for i in range(0,len(temp)):
        if vis[i] == 0 and st != temp[i]:
            vis[i] = 1
            st = temp[i]
            graph[n] = temp[i]
            backtracking(n + 1)
            graph.remove(temp[i])
            vis[i] = 0

N,M = map(int,input().split())
temp = list(map(int,input().split()))
graph = []
vis = [0] * N
temp.sort()
backtracking(0)
