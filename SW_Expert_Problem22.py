# 문제 : 해피박스
# 일정액을 내면 크기가 정해진 박스가 가득 찰 때까지 마음대로 물건을 골라 담을 수 있는 해피박스 이벤트가 열린다고 한다.
# A씨는 박스에 담긴 물건의 가격합계가 최대가 되도록 물건을 담으려고 한다.
# A씨 차례에 남은 물건의 크기와 가격이 주어질 때, A씨가 담을 수 있는 물건 가격은 최대 얼마인지 알아내는 프로그램을 작성하시오.
# 담긴 상품 크기의 합이 박스 크기를 초과할 수 없고, 각 상품은 1개씩 있다. A씨가 고르는 동안 다른 사람이 가져갈 수는 없다.
# 예를 들어 박스의 크기가 10이고 상품의 크기와 가격이 다음과 같다면, 최대로 담을 수 있는 가격 합계는 2번과 3번을 담았을 때인 25이다.
# [입력]
#
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로,
# 첫 줄에 박스의 크기 N과 상품의 개수 M이,
# 이후 M개의 줄에 걸쳐 상품 i의 크기Si와 가격Pi가 주어진다.
# 10<=N<=100, 1<= Si, Pi, M<=20
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

def backtracking(level,scale,value):
    global result
    if level == M:
        result = max(result,value)
        return
    for i in range(M):
        if vis[i] == 1:
            continue
        vis[i] = 1
        if N >= scale+size[i]:
            backtracking(level+1,scale+size[i],value+price[i])
        else:
            backtracking(level+1,scale,value)
        vis[i] = 0


for _ in range(int(input())):
    N,M = map(int,input().split())
    price = []
    size = []
    vis = [0]*M
    result = 0
    for _ in range(M):
        si,pi = map(int,input().split())
        size.append(si)
        price.append(pi)
    backtracking(0,0,0)
    print(result)