from collections import deque

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
            if 0<=nx<100001 and not vis[nx]:
                if nx == x*2 and x != 0:
                    vis[nx] = True
                    queue.appendleft((nx, sec))
                else :
                    vis[nx] = True
                    queue.append((nx, sec+1))


n,k = map(int,input().split())
vis = [False for _ in range(100001)]
bfs()