
def backtracking(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    temp2 = 0

    for i in range(0,len(temp)):
        if temp2 != temp[i]:
            temp2 = temp[i]
            graph.append(temp[i])
            backtracking(n+1)
            graph.pop()


N,M = map(int,input().split())
graph = []
vis = [0] * 10
temp = list(map(int,input().split()))
temp.sort()
backtracking(0)
