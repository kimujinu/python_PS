# 문제 : 전기버스2
# 충전지를 교환하는 방식의 전기버스를 운행하려고 한다.
# 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
# 충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
# 정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오.
# 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.
# 다음은 1번에서 출발 5번이 종점인 경우의 예이다.
# 1번에서 장착한 충전지 용량이 2이므로, 3번 정류장까지 운행할 수 있다.
# 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.
# 마지막 정류장에는 배터리가 없다.
#
#
# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N,
# N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N
# 3
# 5 2 3 1 1
# 10 2 1 3 2 2 5 4 2 1
# 10 1 1 2 1 2 2 1 2 1
# [출력]
# #1 1
# #2 2
# #3 5
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다
import sys

def backtracking(level,value):
    global result
    if value >= N:
        result = min(result,level)
        return
    for i in range(1,N-1):
        if vis[i] == 1:
            continue
        vis[i] = 1
        backtracking(level+1,value+graph[i])
        vis[i] = 0


T = int(input())
for _ in range(T):
    data = list(map(int,input().split()))
    N = data[0]
    graph = data[1:]
    vis = [0]*(N-1)
    result = sys.maxsize
    backtracking(0,graph[0])
    print(result)