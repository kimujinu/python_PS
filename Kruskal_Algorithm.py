# 크루스칼 알고리즘 : 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘,
#                  즉, 최소 비용 신장 트리를 만들기 위한 대표적인 알고리즘이다. 그리디로 분류된다.
# 신장 트리 : 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
#            모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 하다.
#            최소한의 비용으로 구성되는 신장트리르 찾아야 할때, 크루스칼 알고리즘을 이용하여 구현한다.
# 동작과정 : 1) 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
#          2) 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
#               2-1) 사이클이 발생하지 않는 경우, 최소신장트리에 포함시킨다.
#               2-2) 사이클이 발생하는 경우, 최소신장트리에 포함시키지 않는다.
#          3) 모든 간선에 대하여 2번의 과정을 반복한다.
# 성능분석 : 간선의 지수가 E개일때, O(ElogE)의 시간복잡도를 가진다.
#           크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선을 정렬하는 부분이다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노트를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e = map(int,input().split()) # 7 9
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a,b,cost = map(int,input().split()) # 1 2 29, 1 5 75, 2 3 35, 2 6 34, 3 4 7, 4 6 23, 4 7 13, 5 6 53, 6 7 25
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)