#1) 피연산자가들어오면바로출력한다.
#2) 연산자가들어오면자기보다우선순위가높거나같은것들을빼고자신을스택에담는다.
#3) 여는괄호'('를만나면무조건스택에담는다.
#4) 닫는괄호')'를만나면'('를만날때까지 스택에서 출력한다.
#1) 피연산자가들어오면바로출력한다.
#2) 연산자가들어오면자기보다우선순위가높거나같은것들을빼고자신을스택에담는다.
#3) 여는괄호'('를만나면무조건스택에담는다.
#4) 닫는괄호')'를만나면'('를만날때까지 스택에서 출력한다.
import sys

input = sys.stdin.readline

prior = {"/": 2, "*": 2, "+": 1, "-": 1, "(": 0}
stack = []
_str = input().rstrip()

for s in _str:
    if s.isalpha():
        print(s, end="")
    elif s == "(":
        stack.append(s)
    elif s == ")":
        while True:
            temp = stack.pop()
            if temp == "(":
                break
            print(temp, end="")
    else:
        while stack and prior[stack[-1]] >= prior[s]:
            print(stack.pop(), end="")
        stack.append(s)

while stack:
    print(stack.pop(), end="")