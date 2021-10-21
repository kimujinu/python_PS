# 문제 : 연산자 끼워넣기(2)
# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다. 연산자의 개수는 N-1보다 많을 수도 있다. 모든 수의 사이에는 연산자를 한 개 끼워넣어야 하며, 주어진 연산자를 모두 사용하지 않고 모든 수의 사이에 연산자를 끼워넣을 수도 있다.
#
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
#
# 예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 3개, 뺄셈(-) 2개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 250가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.
#
# 1+2+3-4×5÷6
# 1÷2+3+4-5×6
# 1+2÷3×4-5+6
# 1÷2×3-4+5+6
# 1+2+3+4-5-6
# 1+2+3-4-5×6
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.
#
# 1+2+3-4×5÷6 = 1
# 1÷2+3+4-5×6 = 12
# 1+2÷3×4-5+6 = 5
# 1÷2×3-4+5+6 = 7
# 1+2+3+4-5-6 = -1
# 1+2+3-4-5×6 = -18
# N개의 수와 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
import sys

N = int(input())
A_array = list(map(int,input().split()))
B_array = list(map(int,input().split()))

max_v = -sys.maxsize
min_v = sys.maxsize

def dfs(p,m,mul,div,total,level):
    global max_v,min_v
    if len(A_array) == level:
        max_v = max(max_v,total)
        min_v = min(min_v,total)
        return
    else:
        if p > 0:
            dfs(p-1,m,mul,div,total+A_array[level],level+1)
        if m > 0:
            dfs(p,m-1,mul,div,total-A_array[level],level+1)
        if mul > 0:
            dfs(p,m,mul-1,div,total*A_array[level],level+1)
        if div > 0:
            if total < 0:
                temp = -(abs(total)//A_array[level])
                dfs(p,m,mul,div-1,temp,level+1)
            else:
                dfs(p,m,mul,div-1,total//A_array[level],level+1)




dfs(B_array[0],B_array[1],B_array[2],B_array[3],A_array[0],1)

print(max_v)
print(min_v)

