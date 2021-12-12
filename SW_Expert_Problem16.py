# 문제 : 최소 신장 트리 (크루스칼 알고리즘)
# 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
# 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.
# 0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
# 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.
# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
# 다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다.
# 3
# 2 3
# 0 1 1
# 0 2 1
# 1 2 6
# 4 7
# 0 1 9
# 0 2 3
# 0 3 7
# 1 4 2
# 2 3 8
# 2 4 1
# 3 4 8
# 4 6
# 0 1 10
# 0 2 7
# 1 4 2
# 2 3 10
# 2 4 3
# 3 4 10
# 1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000
# [출력]
# #1 2
# #2 13
# #3 22
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(input())):
    V,E = map(int,input().split())
    edges = []
    parents = [i for i in range(V+1)]
    result = 0
    for _ in range(E):
        n1,n2,weight = map(int,input().split())
        edges.append((weight,n1,n2))
    edges.sort()

    for edge in edges:
        weight,n1,n2 = edge
        if find_parent(parents,n1) != find_parent(parents,n2):
            union_parent(parents,n1,n2)
            result += weight

    print(result)


