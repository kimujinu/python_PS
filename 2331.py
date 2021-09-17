

def solution(n,p):
    result[n] += 1
    if result[n] == 3 :
        return
    temp = 0
    for i in str(n):
        temp += int(i) ** p
    solution(temp,p)

result = [0] * (1000001)
A,P = map(int,input().split())
solution(A,P)
result2 = 0
for i in result:
    if i == 1:
        result2 += 1
print(result2)

