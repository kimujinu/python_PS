# 트리의 부모 찾기
# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
vis = [0 for _ in range(N+1)]
for i in range(1,N):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x):
    for i in graph[x]:
        if vis[i] == 0:
            vis[i] = x
            dfs(i)

dfs(1)

for i in range(2,N+1):
    print(vis[i])