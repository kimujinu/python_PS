# Pre-Test 1 차 기출문제
# 문제
# 모든 원소가 0 또는 1 인 행렬이 있습니다. 1 로 표시된 원소는 영역을 나타냅니다. 여기에서 상하좌우에 인접한 1
# 은 같은 영역이라고 가정합니다. 각 영역의 크기는 1 의 개수로 정의합니다. 주어진 N x N 크기의 행렬에서 영역의
# 개수와 각 영역의 크기를 오름차순으로 출력하세요.
# [입력]
# • 첫 번째 행은 행렬의 크기인 N입니다. N 은 1 이상 10 이하의 자연수입니다.
# • 입력 두 번째 행부터는 공백으로 구분된 0 과 1 로 행렬이 주어집니다. 각 행은 개행 문자(newline, \n)로
# 구분됩니다.
# [출력]
# • 첫 번째 행은 영역의 개수를 출력합니다.
# • 두 번째 행은 각 영역의 크기를 공백으로 구분하여 오름차순으로 출력합니다.
# • 한 행의 끝은 불필요한 공백 없이 개행 문자(newline, \n)로 끝나야 합니다.
# • 영역이 존재하지 않을 경우 영역 수 0으로 1 행으로만 출력합니다.

from collections import deque

T = int(input())

graph = []
vis = [[0] * T for _ in range(T)]
array = []

for i in range(T):
    graph.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    vis[x][y] = 1
    result = 1
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= T or ny < 0 or ny >= T:
                continue
            if graph[nx][ny] == 1 and vis[nx][ny] == 0:
                vis[nx][ny] = 1
                result += 1
                queue.append((nx,ny))

    return result

for i in range(T):
    for j in range(T):
        if graph[i][j] == 1 and vis[i][j] == 0:
            array.append(bfs(i,j))

print(len(array))
print(*sorted(array))
