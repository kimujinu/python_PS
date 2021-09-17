
def backtracking(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    st = 0
    temp2 = 0
    if n != 0 :
        st = temp.index(graph[n-1])
    for i in range(st,len(temp)):
        if vis[i] == 0 and temp2 != temp[i]:
            vis[i] = 1
            temp2 = temp[i]
            graph.append(temp[i])
            backtracking(n+1)
            graph.pop()
            vis[i] = 0

N,M = map(int,input().split())
temp = list(map(int,input().split()))
graph = []
vis = [0] * 10
temp.sort()
backtracking(0)