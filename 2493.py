import sys

stack = []
stack_index = []
ans = []
k = int(sys.stdin.readline())
data_list = list(map(int,sys.stdin.readline().split()))
for idx,val in enumerate(data_list):
    while True:
        if len(stack) == 0 :
            stack.append(val)
            stack_index.append(idx + 1)
            ans.append(0)
            break
        if stack[-1] < val:
            stack.pop()
            stack_index.pop()
        else :
            stack.append(val)
            ans.append(stack_index[-1])
            stack_index.append(idx+1)
            break
print(*ans)

