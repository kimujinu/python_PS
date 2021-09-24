from copy import deepcopy

def fill(x,y,arr,d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 6:
                    break
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = '#'
            else:
                break

def dfs(arr,cnt):
    global result
    temp = deepcopy(arr)
    if cnt == cctv_cnt:
        amount = 0
        for i in range(n):
            amount += temp[i].count(0)
        result = min(result, amount)
        return
    x, y, c = cctv[cnt]
    for i in direction[c]:
        fill(x, y, temp, i)
        dfs(temp, cnt+1)
        temp = deepcopy(arr)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            cctv.append([i, j, arr[i][j]])
            
cctv_cnt = len(cctv)
result = int(1e9)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = [[], [[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[3,0]],
             [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]
dfs(arr, 0)
print(result)
