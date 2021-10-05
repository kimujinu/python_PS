
def backtracking(n,value):
    if n == 6:
        print(*temp)
        return
    else:
        for i in range(1,len(array)):
            if vis[i] or value > array[i]:
                continue
            temp.append(array[i])
            vis[i] = 1
            backtracking(n+1,array[i])
            temp.pop()
            vis[i] = 0


while True:
    array = list(map(int,input().split()))
    if array[0] == 0 :
        break
    else:
        temp = []
        vis = [0] * (array[0]+1)
        backtracking(0,0)
        print()