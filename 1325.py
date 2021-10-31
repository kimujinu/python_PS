# 문제 : 효율적인 해킹
# 해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다.
# 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
# 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
# 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

max_value = 0
result = []

#def dfs(i,temp):
#    global max_value
#    temp.append(i)
#    if graph[i] == []:
#        if len(temp)-1 >= max_value:
#            max_value = len(temp)-1
#            result.append(temp[0])
#            return
#    else:
#        for t in graph[i]:
#            if vis[t] == 0:
#                vis[t] = 1
#                dfs(t,temp)
#                vis[t] = 0
#                temp.pop()

ans = []

def bfs(i):
    vis = [0 for _ in range(N+1)]
    vis[i] = 1
    queue = deque()
    queue.append((i))
    count = 1
    while queue:
        x = queue.popleft()
        for j in graph[x]:
            if vis[j] == 0:
                vis[j] = 1
                queue.append((j))
                count += 1
    return count

for i in range(1,N+1):
    temp_result = bfs(i)
    if temp_result > max_value:
        max_value = temp_result
        ans = [i]
    elif temp_result == max_value:
        ans.append(i)
    #vis = [0 for _ in range(N+1)]
    #vis[i] = 1
    #temp = []
    #dfs(i,temp)

print(*ans)

