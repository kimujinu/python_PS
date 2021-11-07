# 문제 : 양치기 꿍
# 양치기 꿍은 맨날 늑대가 나타났다고 마을 사람들을 속였지만 이젠 더이상 마을 사람들이 속지 않는다.
# 화가 난 꿍은 복수심에 불타 아예 늑대들을 양들이 있는 울타리안에 마구 집어넣어 양들을 잡아먹게 했다.
# 하지만 양들은 보통 양들이 아니다. 같은 울타리 영역 안의 양들의 숫자가 늑대의 숫자보다 더 많을 경우 늑대가 전부 잡아먹힌다. 물론 그 외의 경우는 양이 전부 잡아먹히겠지만 말이다.
# 꿍은 워낙 똑똑했기 때문에 이들의 결과는 이미 알고있다. 만약 빈 공간을 '.'(점)으로 나타내고 울타리를 '#', 늑대를 'v', 양을 'k'라고 나타낸다면 여러분은 몇 마리의 양과 늑대가 살아남을지 계산할 수 있겠는가?
# 단, 울타리로 막히지 않은 영역에는 양과 늑대가 없으며 양과 늑대는 대각선으로 이동할 수 없다.
import sys
sys.setrecursionlimit(100000)

R,C = map(int,input().split())
graph = []
vis = [[0]* C for _ in range(R)]
for i in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    global output1,output2
    vis[x][y] = 1
    if graph[x][y] == "k":  # 양
        output1 += 1
    elif graph[x][y] == "v":
        output2 += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C and vis[nx][ny] == 0 and graph[nx][ny] != "#":
            dfs(nx,ny)

result1 = 0
result2 = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] != "#" and vis[i][j] == 0:
            output1 = 0
            output2 = 0
            dfs(i,j)
            if output1 > output2:
                result1 += output1
            else:
                result2 += output2
print(result1, result2)