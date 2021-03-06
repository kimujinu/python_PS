# 문제 : 태권왕
# 태균이는 지금 태권도 겨루기 중이다. 지금은 상대에게 지고 있지만 지금부터 진심으로 경기하여 빠르게 역전을 노리려 한다.
# 태균이가 현재 할 수 있는 연속 발차기는 두가지가 있다.
# A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기이다. 하지만 상대 역시 3점을 득점하는 위험이 있다.
# B는 1점을 얻는 연속 발차기이다.
# 현재 태균이의 점수 S와 상대의 점수 T가 주어질 때, S와 T가 같아지는 최소 연속 발차기 횟수를 구하는 프로그램을 만드시오.
# 입력
# 첫째 줄에 테스트 케이스의 수 C(1 ≤ C ≤ 100)이 주어진다. 둘째 줄부터 C줄에 걸쳐 테스트 케이스별로 현재 점수 S와 T가 공백을 사이에 두고 주어진다. (1 ≤ S < T ≤ 100)
# 출력
# 각 줄마다 S와 T가 같아지는 최소 연속 발차기 횟수를 출력한다.
from collections import deque

def bfs(s,t):
    queue = deque()
    queue.append((s,t,0))
    while queue:
        x,temp_result,counting = queue.popleft()
        if x == temp_result:
            return counting
        if x<=temp_result:
            queue.append((x*2,temp_result+3,counting+1))
            queue.append((x+1, temp_result, counting+1))


for _ in range(int(input())):
    S,T = map(int,input().split())
    print(bfs(S,T))