# 문제 : 진우의 민트초코우유
# 진우는 민트초코우유를 좋아하는 민초단이다. 힘든 일이 있더라도 민트초코우유 하나를 마시면 기운이 펄펄 솟는다고 한다!
# 민트초코우유를 너무 좋아하는 나머지 진우는 매일 아침 특정 지역들에서 민트초코우유가 배달된다는 N × N 크기의 2차원 민초마을로 이사를 하였다.
# 진우는 아침에 눈을 뜨면 집에서 민초마을의 지도를 들고 민트초코우유를 찾으러 출발한다.
# 이때의 초기 체력은 M이다. 여기에서 체력은 진우가 이동할 수 있는 거리를 나타낸다.
# 진우는 지도상에서 상, 하, 좌, 우로 1칸씩 이동할 수 있으며 이동하면 체력이 1만큼 줄어든다.
# 진우가 마을을 돌아다니다가 민트초코우유를 마신다면 체력이 H 만큼 증가하며 진우의 체력이 초기체력 이상으로 올라갈 수 있다.
# 체력이 0이 되는 순간 진우는 이동할 수 없다.
# 민트초코를 찾으러 돌아다니다가 마을 한복판에서 체력이 0이 되어 집으로 못 돌아가는 상황은 만들어져서는 안된다.
# 진우가 얼마나 많은 민트초코우유를 마시고 집으로 돌아올 수 있는지 알아보자.
# 입력
# 첫번째 줄에 민초마을의 크기인 N과 진우의 초기체력 M, 그리고 민트초코우유를 마실때 마다 증가하는 체력의 양 H가 공백을 두고 주어진다. N, M, H는 모두 10보다 작거나 같은 자연수이다.
# 두번째 줄부터 N+1번째 줄에 N칸에 걸쳐서 민초마을의 지도가 주어진다.
# 각 칸은 공백을 두고 주어지며 지도상에서 진우의 집은 1,
# 민트초코우유는 2로 주어지며 빈 땅은 0으로 주어진다.
# 진우의 집은 무조건 한 곳이 주어지며 마을에 배달되는 민트초코우유의 총합은 10개를 넘지 않는다.
# 출력
# 진우가 집을 나와서 다시 집으로 돌아올 때 까지 마실 수 있는 민트초코우유의 최대 개수를 출력하자.


dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M,H = map(int,input().split()) # N:민초마을 크기, M:초기체력, H: 마실때마다 증가하는 체력
graph = []
result = 0
temp = 0
mint_list = []
hx = 0
hy = 0
for i in range(N):
    graph.append(list(map(int,input().split())))

def backtracking(x,y):
    global M,H,temp,result
    for i,j in mint_list:
        if graph[i][j] == 2:
            if M >= abs(x-i) + abs(y-j):
                graph[i][j] = 0
                M += H
                M -= abs(x-i)+abs(y-j)
                temp += 1
                backtracking(i,j)
                M -= H
                M += abs(x-i)+abs(y-j)
                temp -= 1
                graph[i][j] = 2
        elif graph[i][j] == 1:
            if M >= abs(x-i) + abs(y-j):
                result = max(temp,result)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            hx,hy = i,j
            mint_list.append((i,j))
        elif graph[i][j] == 2:
            mint_list.append((i,j))

backtracking(hx,hy)
print(result)
