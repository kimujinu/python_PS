# 문제 : 구간 합 구하기(세그먼트 트리)
# 어떤 N개의 수가 주어져 있다.
# 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다.
# 만약에 1,2,3,4,5 라는 수가 있고,
# 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다.
# 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면
# 12가 될 것이다.
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000),
# (1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고,
# K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다.
# 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데,
# a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.
# 입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.
# 출력
# 첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.
import sys


# 세그먼트 트리 생성
# 노드가 담당하는 구간 [start,end]
def init(node, start, end):
    # 노드가 리프노드인 경우, 배열의 원소 값을 반환
    # 노드가 리프노드인 경우, 리프노드는 배열의 그 원소를 가져야 하기 때문에 tree[node] = a[start]가 된다.
    if start == end:
        tree[node] = graph[start]
        return tree[node]
    else:
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]


# 구간 합 구하기
# 노드가 담당하는 구간 [start,end]
# 합을 구해야하는 구간 [left, right]
def subSum(node, start, end, left, right):
    # 겹치지 않기 때문에, 더 이상 탐색을 이어갈 필요가 없다.
    if left > end or right < start:
        return 0

    # 구해야하는 합의 범위는 [left,right]인데, [start,end]는 그 범위에 모두 포함되고
    # 그 노드의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율적이다.
    if left <= start and end <= right:
        return tree[node]

    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야한다.
    # 노드의 왼쪽 자식은 node*2, 오른쪽 자식은 node*2+1이 된다.
    # 또, 노드가 담당하는 구간이 [start,end]라면 왼쪽 자식은 [start,(start+end)/2], 오른쪽 자식은 [(start+end)/2+1,end)]을 담당
    return subSum(node * 2, start, (start + end) // 2, left, right) + subSum(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff

    # 리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에 검사
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

N,M,K = map(int,sys.stdin.readline().split())
graph = []
tree = [0] * 3000000
for _ in range(N):
    graph.append(int(sys.stdin.readline().rstrip()))

init(1,0,N-1)

for _ in range(M+K):
    A,B,C = map(int,sys.stdin.readline().split())
    if A == 1:
        B = B - 1
        diff = C - graph[B]
        graph[B] = C
        update(1,0,N-1,B,diff)
    elif A == 2:
        print(subSum(1,0,N-1,B-1,C-1))



