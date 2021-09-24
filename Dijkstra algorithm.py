# 다익스트라 알고리즘 : 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단경로를 계산하는 알고리즘
#                    다익스트라 최단경로 알고리즘은 음의 간선이 없을 때 정상동작
#                    그리디 알고리즘으로 분류.(매상황 가장 비용이 적은 노드를 선택해 임의의 과정반복)
# 동작과정 : 1) 출발노드 설정
#           2) 최단 거리 테이블 초기화
#           3) 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택
#           4) 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
#           5) 3,4번 반복
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n,m = map(int,input().split()) # 6, 11
# 시작 노드 번호를 입력받기
start = int(input()) # 1
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
vis = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split()) # 1 2 2, 1 3 5, 1 4 1, 2 3 3, 2 4 2, 3 2 3, 3 6 5, 4 3 3, 4 5 1, 5 3 1, 5 2 6
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not vis[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    vis[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        vis[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

# 다익스트라 알고리즘 특징 : 1) 그리디 알고리즘(매상황에서 방문하지 않은 가장 비용이 적은 노드를 선택하여 반복)
#                        2) 단계를 거치며 한번 처리된 노드의 최단거리는 고정되어 더이상 바뀌지 않는다.
#                        3) 다익스트라 알고리즘을 수행한 뒤 테이블에 각 노드까지의 최단거리 정보가 저장된다.
# 성능분석 : 총 O(V)번에 걸쳐서 최단거리가 가장 짧은 노드를 매번 선형탐색 해야한다. O(V^2)
#           일반적으로 전체노드의 개수가 5000개 이하면 문제해결이 가능하다.
#               -> 하지만 10000개가 넘어가는 경우는 힙(Heap)을 이용해야한다.