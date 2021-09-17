import sys
from collections import deque

N, M = map(int, input().split())  # 행,열

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int,input().split())) for _ in range(N)]

def bfs(x, y, melt, visited):

    queue = deque()
    if visited[x][y]:
        return False
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 인덱스범위를 벗어나면
                continue
            if graph[nx][ny] == 0:  # 새로 탐색한 배열이 바다면
                melt[x][y] += 1
                continue  # 큐에는 추가하면 안되니까
            if not visited[nx][ny]:  # 아직 방문하지 않은 노드라면(빙산만 추가됨)
                queue.append((nx, ny))
                visited[nx][ny] = True

    return True


def oneYearLater():
    check = False  # 전부 녹았는지 확인하는 변수
    melt = [[0] * M for _ in range(N)]  # 1년 후 각각의 빙산이 얼마나 녹는지 저장할 배열
    visited = [[False] * M for _ in range(N)]  # 방문한 노드를 graph에 표시할 경우 melt를 적용하기 어려움
    numberOfIce = 0
    for i in range(1, N):  # 모서리는 바다니까 탐색할 필요없음
        for j in range(1, M):
            if graph[i][j] != 0:
                check = True
                if bfs(i, j, melt, visited):
                    numberOfIce += 1

    for i in range(N):
        for j in range(M):
            graph[i][j] -= melt[i][j]  # 처음 0년은 전혀 녹지않음
            if graph[i][j] < 0:
                graph[i][j] = 0

    return numberOfIce, check


year = -1
while True:
    year += 1
    num, check = oneYearLater()
    if num >= 2:
        print(year)
        break
    if not check:
        print("0")
        break

