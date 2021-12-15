# 문제 : 최소 스패닝 트리(프림 알고리즘)
# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
# 입력
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.
# 그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고,
# 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.
#  3 3
# 1 2 1
# 2 3 2
# 1 3 3
# 출력
# 3
# 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
# * 최소 스패닝 트리(Minimun spanning Tree, MST)는 스패닝 트리 중 가중치 값이 최소인 스패닝 트리를 말한다.
# *  스패닝 트리란 그래프 G의 모든 vertex가 싸이클 없이 연결된 형태를 말한다.
import heapq

V,E = map(int,input().split())
graph = [[] for i in range(V+1)]
vis = [0]*(V+1)

def prim():
    candidate = []
    mst = []
    total_weight = 0
    heapq.heappush(candidate,(0,1))
    while candidate:
        weight,b = heapq.heappop(candidate)
        if vis[b]==1:
            continue
        vis[b] = 1
        mst.append(b)
        total_weight += weight
        for edge in graph[b]:
            if vis[edge[0]] == 0:
                heapq.heappush(candidate,(edge[1],edge[0]))
    return total_weight

for _ in range(E):
    A,B,C = map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

print(prim())

