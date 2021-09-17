
def backtracking(n,i):
    global count
    if n >= N:
        return
    i += temp[n]
    if i == S :
        count += 1
    backtracking(n+1,i - temp[n])
    backtracking(n + 1, i)

N,S = map(int,input().split())
temp = list(map(int,input().split()))
count = 0
backtracking(0,0)
print(count)