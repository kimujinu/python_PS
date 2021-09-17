
def backtracking(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    for i in temp2:
        if vis[i] == 0:
            vis[i] = 1
            graph[n] = i
            backtracking(n+1)
            vis[i] = 0



N,M = map(int,input().split())
temp = map(int,input().split())
temp2 = []
graph = [0] * 10
for i in temp:
    temp2.append(i)
temp2.sort()
vis = [0] * 10000

backtracking(0)

