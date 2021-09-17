import sys

n = int(sys.stdin.readline())
h = [int(sys.stdin.readline()) for _ in range(n)]
stack, cnt = [], 0
for i in range(n):
    while stack and stack[-1] <= h[i]:
        stack.pop()
    stack.append(h[i])
    cnt += len(stack)-1
print(cnt)