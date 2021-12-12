# 문제 : 최소 이동 거리
# A도시에는 E개의 일방통행 도로 구간이 있으며, 각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 붙어있다.
# 구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때, 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.
# 모든 연결 지점을 거쳐가야 하는 것은 아니다.
# 그림은 입력인 N=2, E=3, 시작과 끝 지점, 구간 거리가 아래와 같은 경우의 예이다.
# 0 1 1
# 0 2 6
# 1 2 1
# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 연결지점 번호N과 도로의 개수 E가 주어진다.
# 3
# 2 3
# 0 1 1
# 0 2 6
# 1 2 1
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
# 다음 줄부터 E개의 줄에 걸쳐 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w가 차례로 주어진다. ( 1<=T<=50, 1<=N, s, e<=1000, 1<=w<=10, 1<=E<=1000000 )
# [출력]
# #1 2
# #2 4
# #3 10
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

for _ in range(int(input())):
    N,E = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        graph[s].append((e,w))
    distance = [1e9] * (N+1)
    start_Node = 0
    dijkstra(0)
    print(distance[N])


