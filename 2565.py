
N = int(input())
array = []
for i in range(N):
    A,B = map(int,input().split())
    array.append((A,B))

array.sort()

dp = [1] * N

for i in range(1,len(array)):
    for j in range(i):
        if array[i][1]>array[j][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))