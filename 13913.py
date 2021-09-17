from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(vis[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str,arr[::-1])))

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x= queue.popleft()
        if x == k :
            print(vis[x])
            path(x)
            break
        for nx in (x-1,x+1,x*2):
            if 0<=nx<100001 and vis[nx]==0:
                 vis[nx] = vis[x] + 1
                 queue.append(nx)
                 move[nx] = x


n,k = map(int,input().split())
vis = [0 for _ in range(100001)]
move = [0 for _ in range(100001)]
bfs()