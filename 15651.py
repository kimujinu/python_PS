

def solution(n):
    if n == M :
        for i in range(M):
            print(graph[i],end=' ')
        print()
        return
    for i in range(1,N+1):
        graph[n] = i
        solution(n+1)

N,M = map(int,input().split())
graph = [0] * 10
solution(0)