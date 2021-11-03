# 문제 : 물통
# 각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다. 처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다.
# 이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데, 이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다.
# 이 과정에서 손실되는 물은 없다고 가정한다.
# 이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다.
# 첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 세 정수 A, B, C가 주어진다.
# 출력
# 첫째 줄에 공백으로 구분하여 답을 출력한다. 각 용량은 오름차순으로 정렬한다.
from collections import deque

A,B,C = map(int,input().split())
result = []
vis = [[0]*201 for _ in range(201)]
queue = deque()
queue.append((0,0))

# x, y의 경우의 수 저장
def check(x, y):
    if not vis[x][y]:
        vis[x][y] = True
        queue.append((x, y))

def bfs():

    while queue:
        # x : a물통의 물의 양, y : b물통의 물의 양, z : c물통의 물의 양
        x, y = queue.popleft()
        z = C - x - y

        # a 물통이 비어있는 경우 c 물통에 남아있는 양 저장
        if x == 0:
            result.append(z)

        # x -> y
        water = min(x, B-y)
        check(x - water, y + water)
        # x -> z
        water = min(x, C-z)
        check(x - water, y)
        # y -> x
        water = min(y, A-x)
        check(x + water, y - water)
        # y -> z
        water = min(y, C-z)
        check(x, y - water)
        # z -> x
        water = min(z, A-x)
        check(x + water, y)
        # z -> y
        water = min(z, B-y)
        check(x, y + water)

bfs()


for i in sorted(set(result)):
    print(i,end=' ')




