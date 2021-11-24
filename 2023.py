# 문제 : 신기한 소수
# 수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.
# 7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.
# 수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.
# 출력
# N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.
import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

N = int(input())

def backtracking(level,temp):
    if level == N:
        for i in temp:
            print(i,end='')
        print()
        return
    for i in range(1,10):
        temp += str(i)
        if not is_prime_number(int(temp)):
            temp = temp[:-1]
            continue
        backtracking(level+1,temp)
        temp = temp[:-1]


backtracking(0,'')