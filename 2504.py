import sys

check = False
total = 0
mul = 1
result = []
str ="(()[[]])([])"#sys.stdin.readline().rstrip()
for i in range(len(str)) :
    if str[i] == '(':
        mul *= 2
        result.append(str[i])
    elif str[i] == '[':
        mul *= 3
        result.append(str[i])
    elif str[i] == ')':
        if not result or result[-1] != '(' :
            check = True
            break
        else :
            if str[i-1] == '(':
                total += mul
            result.pop()
            mul //= 2
    elif str[i] == ']':
        if not result or result[-1] != '[' :
            check = True
            break
        else :
            if str[i-1] == '[' :
                total += mul
            result.pop()
            mul //= 3

if check or len(result) > 0 :
    print("0")
else :
    print(total)