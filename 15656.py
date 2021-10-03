
def backtracking(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    for i in temp2:
        graph[n] = i
        backtracking(n+1)


N,M = map(int,input().split())
temp = map(int,input().split())
graph = [0] * 10
temp2 = []
for i in temp:
    temp2.append(i)

temp2.sort()
backtracking(0)