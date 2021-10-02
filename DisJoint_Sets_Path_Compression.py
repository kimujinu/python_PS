# 서로소 집합(DisJoint Sets) : 공통원소가 없는 두 집함, 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
#                           두 종류 연산을 지원 : 합집합(두개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산)
#                                               찾기(특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산)
# 기본적 구현의 문제점을 해결하기 위해 경로 압축 실행 : 찾기 함수를 재귀적으로 호출한 뒤 부모테이블 값을 바로 갱신한다.
#                                               경로 압축기법을 적용하면 각 노드에 대하여 찾기 함수를 호출한 이후에 해당 노드의 루트 노드가 바로 부모노드가 된다.


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

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합 ',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ',end='')
for i in range(1,v+1):
    print(parent[i],end=' ')