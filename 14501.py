from itertools import combinations

def recursion(day,sum):
    global result
    if day == N + 1:# 기저조건
        result  = max(sum,result)
        return

    if day > N + 1: #상담 불가능, 퇴사날을 넘어가는 경우
        return

    recursion(day+Ti[day],sum+Pi[day])#상담

    recursion(day+1,sum) #상담안함

N = int(input())
Ti = [0] * (N+1)
Pi = [0] * (N+1)

for i in range(1,N+1):
    T,P = map(int,input().split())
    Ti[i] = T
    Pi[i] = P

result = 0
recursion(1,0)
print(result)