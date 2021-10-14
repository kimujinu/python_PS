from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y,1))
    vis = [[[0]*2 for _ in range(M)] for _ in range(N)]
    vis[x][y][1] = 1
    while queue :
        x,y,z = queue.popleft()
        if x==N-1 and y==M-1:
            return vis[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # vis[x][y][z]에서 z가 0이라면 벽을 한번 뚫은 상태, 1이라면 아직 기회가 있음.
            if 0<= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and z == 1 :
                    vis[nx][ny][0] = vis[x][y][1] + 1
                    queue.append((nx,ny,0))
                if graph[nx][ny] == 0 and vis[nx][ny][z] == 0 :
                    vis[nx][ny][z] = vis[x][y][z] + 1
                    queue.append((nx,ny,z)) 
    return -1


dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
print(bfs(0,0))