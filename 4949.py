import sys

while True :
    temp = sys.stdin.readline().rstrip()
    if temp == '.':
        break
    result = []
    for s in temp :
        if s == '(' or s == '[' :
            result.append(s)
        elif s == ']':
            if not result or result.pop() != '[':
                result.append(s)
                break
        elif s == ')':
            if not result or result.pop() != '(':
                result.append(s)
                break
    if not result :
        print('yes')
    else :
        print('no')