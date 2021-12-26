# 문제 : 사람 네트워크2
# 어떤 사화과학 연구 단체에서 사람의 네트워크에 대하여 여러 가지 측정 방법을 사용하여 연구하기로 하였다.
# 이를 위해 우선 주어진 사람 네트워크에서 누가 가장 영향력이 있는 사람인지를 알 수 있는 척도로서 다음을 분석하는 프로그램을 작성하시오.
# 단, N은 입력 사람 네트워크 (그래프)의 노드 수이다.
# Closeness Centrality(CC):Closeness는 네트워크 상에서 한 사용자가 다른 모든 사람에게 얼마나 가까운가를 나타낸다.
# 따라서 사용자 i의 CC(i)는 다음과 같이 계산된다.
#       CC(i) = ∑ j dist(i,j) 단, dist(i,j)는 노드i로부터 노드 j까지의 최단 거리이다.
# 예제 1)
# 위의 예제는 사람 네트워크에서 사용자 2의 dist합이 가장 작으며, CC(2) = 4임을 통해 사용자 2가 모든 다른 사용자들로부터 가장 가까운 사용자이다.
# 예제 2)
# 위의 예제는 사람 네트워크에서 사용자 3의 dist합이 가장 작으며, CC(3) = 5임을 통해 사용자 3이 모든 다른 사용자들로부터 가장 가까운 사용자이다.
# [제약 사항]
# 입력으로 주어지는 사람 네트워크에서 노드 자신을 연결하는 간선은 없다.
# 또한 사람 네트워크는 하나의 연결 요소(connected component)로 구성되어 있다.
# 단, 사람 네트워크의 최대 사용자 수는 1,000 이하이다.
#
# 테스트 케이스들은 아래의 그룹들로 이루어져 있다.
# 그룹 1 싸이클이 없고 N <= 10 인 경우
# 그룹 2 싸이클이 없고 10 < N <= 100 인경우
# 그룹 3 싸이클이 있고 N<= 10
# 그룹 4 싸이클이 있고10 < N <= 100
# 그룹 5 모든 경우가 존재하고 100 < N <= 1000
#
# [입력]
#
# 맨 위의 줄에는 전체 테스트 케이스의 수 T가 주어진다.
#
# 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
#
# 각 테스트 케이스는 한 줄에 주어지며, 사람 수인 양의 정수 N이 주어진 다음, 사람 네트워크의 인접 행렬이 행 우선 (row-by-row) 순으로 주어진다.
#
# 단, 각 숫자 사이에는 1개의 공백이 주어진다.
#
# [출력]
#
# 총 T줄에 T개의 테스트 케이스 각각에 대한 답을 한 줄에 출력한다.
#
# 각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 사람 그래프에서 사람들의 CC 값들 중에서 최솟값을 한 줄에 출력한다.

def dijkstra(x):
    global result
    temp_array = []
    temp_total = 0
    vis = [0]*N
    vis[x] = 1
    for i in vertex[x]: # 직접적으로 연결된 노드 방문체크 및 거리추가
        vis[i] = 1
        temp_array.append((i,1))
        temp_total += 1
    while vis.count(0):
        now,dist = temp_array.pop()
        for i in vertex[now]:
            if vis[i]==1:
                continue
            vis[i] = 1
            temp_total += dist + 1
            temp_array.append((i,dist+1))

    if result > temp_total:
        result = temp_total
        return



for _ in range(int(input())):
    temp = list(map(int,input().split()))
    N = temp[0]
    vertex = []
    result = 1e9
    graph = []
    for i in range(1,len(temp),N):
        graph.append(temp[i:i+N])
    for i in range(N):
        temp2 = []
        for j in range(N):
            if graph[i][j] == 1:
                temp2.append(j)
        vertex.append(temp2)

    for i in range(N):
        dijkstra(i)

    print(result)
