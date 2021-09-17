from collections import deque

def valid(n) :
    if n < 0 or n > 100000 or vis[n]:
        return False
    return True

def bfs():
    sec = 0
    queue = deque()
    queue.append((n,sec))
    while queue:
        x,sec = queue.popleft()
        if x == k :
            print(sec)
            break
        for nx in (x-1,x+1,x*2):
            if valid(nx):
                vis[nx] = True
                queue.append((nx,sec+1))


n,k = map(int,input().split())
vis = [False for _ in range(100001)]
bfs()