from collections import Counter

N = int(input())
temp = list(map(int,input().split()))
temp2 = Counter(temp)
permute = [-1] * N
stack = []

stack.append(0)

for i in range(1,N):
    while stack and temp2[temp[stack[-1]]] < temp2[temp[i]]:
        permute[stack.pop()] = temp[i]
    stack.append(i)

print(*permute)
