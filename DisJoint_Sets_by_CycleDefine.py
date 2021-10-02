# 서로소 집합을 활용한 사이클 판별 : 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할때 사용할 수 있다.(DFS)
#   사이클 판별 알고리즘 동작과정 : 1) 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인한다.
#                                   1-1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합 연산을 수행
#                                   1-2) 루트 노드가 서로 같다면 사이클이 발생한 것
#                              2) 그래프에 포함되어 있는 모든 간선에 대하여 1번과정을 반복

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

v,e = map(int,input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a,b = map(int,input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 연산 수행
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생안함")