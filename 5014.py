from collections import deque


def bfs():
    count = 0
    queue = deque()
    queue.append((S,count))
    vis[S] = True
    while queue:
        s,count = queue.popleft()
        if s == G :
             return count
        for nx in (s + U,s - D):
             if 1<=nx<=F and not vis[nx] :
                vis[nx] = True
                queue.append((nx,count+1))

    return "use the stairs"


F,S,G,U,D = map(int,input().split())
vis = [False  for _ in range(F+1)]
print(bfs())