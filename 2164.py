import sys
from collections import deque

data_list = deque([i+1 for i in range(int(sys.stdin.readline()))])
while len(data_list) > 1 :
    data_list.popleft()
    data_list.append(data_list.popleft())
print(*data_list)
