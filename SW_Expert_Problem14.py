# 문제 : 연산
# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
# 단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
# 예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.
# [입력]
# 첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M
# 3
# 2 7
# 3 15
# 36 1007
# [출력]
# #1 3
# #2 4
# #3 8
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
from collections import deque


def bfs(N,M):
    queue = deque()
    queue.append((N,0))
    while queue:
        x,count = queue.popleft()
        if x == M :
            return count
        for i in (x+1,x-1,x*2,x-10):
            if 0<i<100001:
                queue.append((i,count+1))

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    print(bfs(N,M))