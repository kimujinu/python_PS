# 문제 : 연구소
# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
#
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
#
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

from collections import deque
from itertools import combinations
from copy import deepcopy

N,M = map(int,input().split())
graph = []
zero = []
virus = []

for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(M):
        if graph[i][j] == 0:
            zero.append((i,j))
        elif graph[i][j] == 2:
            virus.append((i,j))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    tempGraph = deepcopy(graph)
    queue = deque(virus)

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if tempGraph[nx][ny] == 0:
                tempGraph[nx][ny] = 2
                queue.append((nx,ny))

    count = 0
    for i in range(N):
        count += tempGraph[i].count(0)
    return count

result = 0
for data in combinations(zero,3):
    for x,y in data:
        graph[x][y] = 1
    result = max(result,bfs())
    for x,y in data:
        graph[x][y] = 0

print(result)