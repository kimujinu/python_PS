
def backtracking(n):
    if n == M:
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    st = 0
    if n != 0:
        st = temp2.index(graph[n-1])
    for i in range(st,len(temp2)):
         graph[n] = temp2[i]
         backtracking(n+1)

N,M = map(int,input().split())
temp = map(int,input().split())
graph = [0] * 10
temp2 = []
for i in temp:
    temp2.append(i)
temp2.sort()
backtracking(0)
