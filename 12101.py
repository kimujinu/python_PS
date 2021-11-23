# 문제 : 1,2,3 더하기 2
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
#
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 이를 사전순으로 정렬하면 다음과 같이 된다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 1+3
# 2+1+1
# 2+2
# 3+1
# 정수 n과 k가 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법 중에서 k번째로 오는 식을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 n과 k가 주어진다. n은 양수이며 11보다 작고, k는 231-1보다 작거나 같은 자연수이다.
#
# 출력
# n을 1, 2, 3의 합으로 나타내는 방법 중에서 사전 순으로 k번째에 오는 것을 출력한다. k번째 오는 식이 없는 경우에는 -1을 출력한다.

N,K = map(int,input().split())
result = []
temp2 = 0
temp = []
def bt(value):
    global N,K,result,temp2
    if sum(value) == N:
        temp2 += 1
        if temp2 == K:
            for i in range(len(value)):
                if i == len(value)-1:
                    print(value[i],end='')
                else:
                    print(value[i],end='+')
            exit(0)
        return
    if sum(value) > N :
        return
    for i in range(1,4):
        temp.append(i)
        bt(temp)
        temp.pop()

bt(temp)
print(-1)