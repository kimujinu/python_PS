# 문제 : 어드벤처 게임
# 어드벤처 게임을 하던 중, 1부터 n까지의 번호가 붙은 방을 지나가야 하는 마법의 미로를 마주쳤다.
# 각 방 안에는 번호가 붙은 문이 있을 수 있고, 각 문은 해당하는 번호의 방으로 통한다. 방 안에는 레프리콘이나 트롤이 있을 수도 있다.
# 레프리콘이 있는 방에 들어가면 레프리콘은 모험가의 소지금이 일정 양 이하로 떨어지지 않게 채워준다.
# 레프리콘은 모험가의 소지금이 일정량 미만일 때에는 그만한 양이 되도록 금화를 채워주고, 소지금이 일정량 이상일 때에는 그대로 둔다.
# 트롤이 있는 방에 들어가려면 일정량의 통행료를 지불해야 한다. 이는 맨 처음에 모험가가 1번 방에서 시작하려 할 때에도 마찬가지이다.
# 모험가는 소지금이 0인 상태에서 출발한다. 과연 모험가는 1번 방에서 출발해서 n번 방에 도착할 수 있을까?
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node,money,n):
    global flag,vis
    if typeList[node] == 'L':
        if money < payList[node]:
            money = payList[node]
    elif typeList[node] == "T":
        if money < payList[node]:
            return
        else:
            money -= payList[node]

    if node == n :
        flag = True
        return

    for next_node in nodeGraph[node]:
        if not vis[next_node]:
            vis[next_node] = 1
            dfs(next_node,money,n)
            vis[next_node] = 0
    return

while True :
    flag = False
    typeList = [0]
    payList= [0]
    n = int(input())
    nodeGraph = [[] for _ in range(n+1)]
    if n == 0 :
        exit(0)
    for i in range(1,n+1):
        temp_input = sys.stdin.readline().split()
        typeList.append(temp_input.pop(0))
        payList.append(int(temp_input.pop(0)))
        temp_list= list(map(int,temp_input[:-1]))
        for j in temp_list:
            nodeGraph[i].append(j)

    vis = [0 for _ in range(n+1)]

    dfs(1,0,n)
    if flag:
        print("Yes")
    else:
        print("No")

