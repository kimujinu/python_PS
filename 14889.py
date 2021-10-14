import sys

N = int(input())
array = [list(map(int,input().split())) for _ in range(N)]
vis = [0] * N
result = sys.maxsize

def backtracking(idx,cnt):
    global result
    if cnt == N//2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if vis[i] and vis[j]:
                    start += array[i][j]
                elif not vis[i] and not vis[j]:
                    link += array[i][j]
        result = min(result,abs(start-link))
        return

    for i in range(idx,N):
        if vis[i] :
            continue
        vis[i] = 1
        backtracking(i+1,cnt+1)
        vis[i] = 0

backtracking(0,0)
print(result)