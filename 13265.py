# 문제 : 색칠하기
# 어린 토니킴은 색칠공부를 좋아한다.
# 토니킴은 먼저 여러 동그라미와 동그라미 두 개를 연결하는 직선들 만으로 그림을 그리고 (모든 동그라미들 사이에 직선이 있을 필요는 없다),
# 연결된 두 동그라미는 서로 색이 다르게 되도록 색을 칠하고자 한다.
# 이 그림을 색칠하는데 필요한 최소의 색의 개수를 구하는 문제는 어렵기 때문에 토니킴은 2 가지 색상으로 색칠이 가능한지의 여부만을 알고 싶어한다.
# 동그라미들의 번호와 동그라미들이 서로 연결된 직선에 대한 정보가 주어졌을 때, 이 동그라미들이 2 가지 색상으로 색칠이 가능한지 알아내자.
import sys

def dfs(x,pre_value):
    global flag
    if vis[x] == 0:
        vis[x] = pre_value
        for i in graph[x]:
            dfs(i,3-pre_value)
    else:
        if vis[x] != pre_value:
            flag = False
            return

for i in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    vis = [0 for _ in range(n+1)]
    for j in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    flag = True
    for k in range(1,n+1):
        if vis[k] == 0:
            dfs(k,1)
    print("possible" if flag else"impossible")
