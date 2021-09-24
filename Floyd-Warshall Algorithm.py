# 플로이드 워셜 알고리즘 : 모든 노드에서 다른 모든 노드까지의 최단경로를 모두 계산한다.
#                      다익스트라 알고리즘과 마찬가지로 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행한다.
#                           -> 다만 매단계마다 방문하지 않은 노드중 최단거리를 찾는 과정이 필요하지 않다.
#                       2차원 테이블에 최단거리 정보를 저장한다.
#                       DP 유형에 해당된다.
#                       노드의 개수, 간선의 개수가 적을 때 사용해야 효율적이다.
# 동작과정 : 각 단계마다, 특정한 노드 k를 거쳐가는 경우를 확인한다.
#           a에서 b로가는 최단거리보다 a에서 k로 거쳐 b로가는거리가 더 짧은지 검사한다.
#           D_ab = min(D_ab,D_ak+D_kb) 기본 점화식.
#           1) 그래프 준비 및 최단거리 테이블 초기화
#           2) 1번 노드를 거쳐가는 경우를 고려하여 테이블 갱신
#           3) 2번 노드를 거쳐가는 경우를 고려하여 테이블 갱신...반복

INF = int(1e9)
# 노드의 개수 및 간선의 개수 입력받기
n,m = map(int,input().split()) # 4, 7
# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,c = map(int,input().split()) # 1 2 4, 1 4 6, 2 1 3, 2 3 7, 3 1 5, 3 4 4, 4 3 2
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

# 수행된 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print("무한",end=' ')
        # 도달할 수 있는 경우 거리 출력
        else:
            print(graph[a][b],end=' ')
    print()

# 성능분석 : 노드 개수가 N개 일때 알고리즘 상으로 N번의 단계를 수행한다.
#           -> 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려한다.
#           시간복잡도는 O(N^3)이다.
