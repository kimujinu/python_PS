
N = int(input())
array = list(map(int,input().split()))
temp = []
vis = [0] * N
temp2 = []
result = 0
def backtracking(cnt):
    global result
    if N == cnt :
        total = 0
        for i in range(2,len(temp)+1):
            total += abs(temp[i-2]-temp[i-1])
        temp2.append(total)
        return
    else:
        for i in range(len(array)):
            if vis[i]:
                continue
            temp.append(array[i])
            vis[i] = 1
            backtracking(cnt+1)
            temp.pop()
            vis[i] = 0

backtracking(0)
print(max(temp2))