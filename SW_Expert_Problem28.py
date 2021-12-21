# 문제 : 그래프 색칠하기
# N개의 노드로 구성된 그래프의 노드를 M개의 색상을 이용해 칠하려고 한다.
# 그래프에 대한 정보가 주어지면 모든 인접한 노드 쌍에 대해, 두 노드를 서로 다른 색으로 칠하는 것이 가능한지 알아내는 프로그램을 만드시오.
# 노드 번호는 1에서 N번까지이고, M은 2, 3, 4 중 하나이다. 칠할 수 있는 경우 1, 칠할 수 없는 경우 0을 출력한다.
# 다음은 2가지 색으로 칠할 수 있는 그래프와 칠할 수 없는 그래프의 예이다.
# 왼쪽의 경우 1, 오른 쪽의 경우 0을 출력한다.
# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 노드의 개수 N, 간선의 개수 E,
# 사용할 수 있는 색상수 M이 주어지고, E개의 줄에 걸쳐 간선의 양끝 노드 번호가 주어진다.
# 3<=N<=20, 2<=E<=100, 2<=M<=4
# 2
# 4 4 2
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5 2
# 1 2
# 1 3
# 2 4
# 3 4
# 2 3
# [출력]
# #1 1
# #2 0
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

def dfs(x,pre_values):
    global flag
    if vis[x] == 0:
        vis[x] = pre_values
        for i in graph[x]:
            dfs(i,3-pre_values)
    else:
        if vis[x] != pre_values:
            flag = False
            return

for _ in range(int(input())):
    N,E,M = map(int,input().split())
    graph = [[] for _ in range(E+1)]
    vis = [0] * (N+1)
    flag = True
    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,N+1):
        if not vis[i]:
            dfs(i,1)
    print(1 if flag else 0)
