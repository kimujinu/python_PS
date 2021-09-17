import sys

result = 0
stack = []
data_list = list(sys.stdin.readline().rstrip())
for i in range(len(data_list)):
	if data_list[i] == '(':
		stack.append(i)
	else :
		if data_list[i-1] == '(':
			stack.pop()
			result += len(stack)
		else :
			stack.pop()
			result += 1
print(result)