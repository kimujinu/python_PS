
def backtracking(n):
    if n==M:
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    st = 0
    if n != 0 :
        st = temp2.index(graph[n-1])
    for i in range(st,len(temp2)):
        if vis[temp2[i]] == 0:
            vis[temp2[i]] = 1
            graph[n] = temp2[i]
            backtracking(n+1)
            vis[temp2[i]] = 0

N,M = map(int,input().split())
temp = map(int,input().split())
temp2 = []
graph = [0] * 10
vis = [0] * 10000
for i in temp:
    temp2.append(i)
temp2.sort()
backtracking(0)
