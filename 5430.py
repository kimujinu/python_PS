from sys import stdin as s
from collections import deque

a = s.readline().rstrip()
t = int(a)

for i in range(t):
    tf = True
    r = 0
    cmd = s.readline().rstrip()
    l = int(s.readline().rstrip())
    if l == 0:
        lst = []
        s.readline().rstrip()
    else:
        tmp = s.readline().rstrip()
        tmp = tmp[1:len(tmp) - 1]
        lst = tmp.split(",")

    lst = deque(lst)
    for j in range(len(cmd)):
        if cmd[j] == "R":
            r += 1
        else:
            if len(lst) == 0:
                tf = False
                break
            else:
                if r % 2 == 1:
                    lst.pop()
                else:
                    lst.popleft()

    if r % 2 == 1:
        lst.reverse()
    if tf == False:
        print("error")
    else:
        print("[", end="")
        print(",".join(lst), end="")
        print("]")