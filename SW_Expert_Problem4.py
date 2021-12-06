# 문제 : 최소합
# 그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
#
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
# 그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.
#
# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
# 3
# 3
# 1 2 3
# 2 3 4
# 3 4 5
# 4
# 2 4 1 3
# 1 1 7 1
# 9 1 7 10
# 5 7 2 4
# 5
# 6 7 1 10 2
# 10 2 7 5 9
# 9 3 2 9 6
# 1 6 8 2 9
# 8 3 8 2 1
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
# #1 15
# #2 18
# #3 33
import sys

dx = [0,1]
dy = [1,0]

def dfs(level,x,y,value):
    global result
    value += graph[x][y]
    if level == 2*N-1:
        result = min(result,value)
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            dfs(level+1,nx,ny,value)


for _ in range(int(input())):
    N = int(input())
    graph = []
    result = sys.maxsize
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    dfs(1,0,0,0)
    print(result)