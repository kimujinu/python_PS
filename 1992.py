

def dfs(x,y,n):
    if n == 1 :
        return graph[x][y]
    n = n//2

    r1 = dfs(x,y,n)
    r2 = dfs(x+n,y,n)
    r3 = dfs(x,y+n,n)
    r4 = dfs(x+n,y+n,n)

    if r1 == r2 == r3 == r4 and len(r1)==1:
        return r1

    return "("+r1+r2+r3+r4+")"


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(dfs(0,0,n))
