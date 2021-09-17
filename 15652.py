
def backTracking(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    temp = graph[n-1]
    if n == 0 :
        temp = 1
    for i in range(temp,N+1):
        graph[n] = i
        backTracking(n+1)




N,M = map(int,input().split())
graph = [0] * 10
vis = [0] * 10
backTracking(0)