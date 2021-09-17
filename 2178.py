from collections import deque

# BFS 소스코드 구현
def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y]+1


# n,m을 공백을 기준으로 구분하여 입력 받기
n,m = 4,6#map(int,input().split())

# 2차원 리스틔의 맵 정보 입력 받기
graph = [
    [1,0,1,1,1,1],
    [1,0,1,0,1,0],
    [1,0,1,0,1,1],
    [1,1,1,0,1,1],
]
#for i in range(n):
 #   graph.append(list(map(int,input())))

# 이동할 네 가지 방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 출발
bfs(0,0)
print(graph[n-1][m-1])

for i in range(4):
    print()
    for j in range(6):
        print(graph[i][j],end=' ')