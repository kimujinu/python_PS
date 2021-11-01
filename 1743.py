# 문제 : 음식물 피하기
# 코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다.
# 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다.
# 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다.
# 이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다.
# 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다.
# 통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다.
# 선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.
# 입력
# 첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ N×M)이 주어진다.  그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.
# 좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다. 입력으로 주어지는 좌표는 중복되지 않는다.
# 출력
# 첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라.
import sys
sys.setrecursionlimit(100000)

N,M,K = map(int,input().split())
graph = [[0]*(M+1) for _ in range(N+1)]
vis = [[0]*(M+1) for _ in range(N+1)]
result = 0
for i in range(K):
    r,c = map(int,input().split())
    graph[r][c] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global temp
    if x <= -1 or x >= N+1 or y <= -1 or y >= M+1:
        return False
    if vis[x][y] == 0 and graph[x][y] == 1:
        vis[x][y] = 1
        temp += 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
    return temp


for i in range(1,N+1):
    for j in range(1,M+1):
        if vis[i][j] == 0 and graph[i][j] == 1:
          temp = 0
          result = max(dfs(i,j),result)

print(result)

