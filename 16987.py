# 문제 : 계란으로 계린치기

N = int(input())
array = [[0]*N for _ in range(N)]
for i in range(N):
    array[i] = list(map(int,input().split()))

result = 0

def dfs(level,array):
    global result
    if len(array) == level:
        count = 0
        for i in range(len(array)):
            if array[i][0] <= 0:
                count += 1
        result = max(result,count)
        return
    if array[level][0] <= 0:
        dfs(level+1,array)
    else:
        for i in range(len(array)):
            flag = False
            if array[i][0]<=0 or i==level:
                continue
            array[level][0] -= array[i][1]
            array[i][0] -= array[level][1]
            flag = True
            dfs(level+1,array)
            array[level][0] += array[i][1]
            array[i][0] += array[level][1]
        if not flag:
            dfs(level+1,array)
    return

dfs(0,array)
print(result)