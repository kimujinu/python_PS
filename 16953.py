# 문제 : A -> B
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
#
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
#
# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.
#
# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다.
# 만들 수 없는 경우에는 -1을 출력한다.
from collections import deque

A,B = map(int,input().split())

def bfs():
    queue = deque()
    queue.append((A,1))
    while queue:
        value, count = queue.popleft()
        if value == B:
            print(count)
            exit(0)
        for i in (value*2,int(str(value)+str(1))):
            if i <= B:
                queue.append((i,count+1))
bfs()
print(-1)