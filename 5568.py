
n = int(input())
k = int(input())
array = []
total = []
temp = []
vis = [0] * n
for i in range(n):
    array.append(int(input()))

def backtracking(n):
    if n == k:
        total.append(''.join(map(str,temp)))
        return
    else:
        for i in range(len(array)):
            if vis[i]:
                continue
            temp.append(array[i])
            vis[i] = 1
            backtracking(n+1)
            temp.pop()
            vis[i] = 0

backtracking(0)
print(len(set(total)))