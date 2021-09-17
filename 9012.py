import sys

for i in range(int(input())) :
    result = []
    ans = "YES"
    str = sys.stdin.readline().rstrip()
    for j in str :
        if j == '(':
           result.append(j)
        elif j == ')':
            if len(result) == 0:
                ans = "NO"
            else :
                result.pop()
    if len(result) > 0 :
        ans = "NO"
    print(ans)
