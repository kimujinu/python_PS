# 문제 : 이분 그래프
# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
# 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
# 입력
# 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
# 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.
# 출력
# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

def dfs(now, group):
    vis[now] = group
    for i in arr[now]:
        # 아직 안가본 곳이면 방문
        if vis[i] == 0:
            if not dfs(i, -group):
                return False
        # 방문한 곳인데 색깔이 다르면 취소
        elif vis[i] == vis[now]:
            return False
    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v + 1)]
    vis = [0] * (v + 1)
    for _ in range(e):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    ans = True
    for i in range(1, v + 1):
        if vis[i] == 0:
            ans = dfs(i, 1)
            if not ans:
                break
    print("YES" if ans else "NO")