
# 분할 정복
def solution(N, start, end):
    if N == 1 :
        print(start, end)
        return
    else :
        solution(N-1,start,6-start-end)
        print(start, end)
        solution(N-1,6-start-end,end)

N = int(input())
print(2**N-1)
solution(N,1,3)