from collections import deque

# 시작점이 여러 개일 때

# 이동할 네 가지 방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0<= ny < n and graph[nx][ny]==0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


n,m = map(int,input().split())

graph = []
queue = deque([])

for i in range(m):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            queue.append([i, j])
bfs()

result = 0

#for i in range(m):
 #   print()
  #  for j in range(n):
   #     print(graph[i][j],end=' ')

for i in graph :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
        else :
            result = max((map(max,graph)))

print(result-1)