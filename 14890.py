# 문제 : 경사로
# 크기가 N×N인 지도가 있다. 지도의 각 칸에는 그 곳의 높이가 적혀져 있다.
#
# 오늘은 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려고 한다. 길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것이다.
# 길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 경사로는 높이가 항상 1이며, 길이는 L이다. 또, 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.
#
# 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
# 아래와 같은 경우에는 경사로를 놓을 수 없다.
#
# 경사로를 놓은 곳에 또 경사로를 놓는 경우
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 경사로를 놓다가 범위를 벗어나는 경우

N,L = map(int,input().split())
graph2 = []
graph3 = [[0]*N for _ in range(N)]
count = 0
for i in range(N):
    graph2.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        graph3[i][j] = graph2[j][i]

def solve(graph):
    vis = [False] * N
    cnt = 1
    for data in range(N-1):
        cur_value, next_value = graph[data],graph[data+1]
        if cur_value != next_value:
            if cur_value > next_value:
                if cur_value-1 != next_value:
                    return False
                if data+L < N:
                    for i in range(1,L+1):
                        if next_value == graph[data+i]:
                            vis[data+i] = True
                        else:
                            return False
                else:
                    return False
            else:
                if cnt < L or cur_value + 1 != next_value or vis[data]:
                    return False
            cnt = 1
        else:
            if vis[data] == False:
                cnt += 1
    return True

for i in graph2:
    if solve(i):
        count += 1
for i in graph3:
    if solve(i):
        count += 1

print(count)



