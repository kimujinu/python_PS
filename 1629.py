
# 분할 정복
def solution(A,B,C):
    if B == 1 :
        return A % C
    else :
        temp = solution(A,B//2,C)
        if B%2 == 0 :
            return temp * temp % C
        else :
            return temp * temp * A % C

A,B,C = map(int,input().split())
print(solution(A,B,C))