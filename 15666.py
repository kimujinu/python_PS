
def backtracking(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    temp2 = 0
    st = 0
    if n != 0 :
        st = temp.index(graph[n-1])
    for i in range(st,len(temp)):
        if temp2 != temp[i]:
            temp2 = temp[i]
            graph.append(temp[i])
            backtracking(n+1)
            graph.pop()


N,M = map(int,input().split())
temp = list(map(int,input().split()))
graph = []
vis = [0] * 10
temp.sort()
backtracking(0)