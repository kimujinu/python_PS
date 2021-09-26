# 문제 : 효율적인 화폐 구성
#       N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록하려고 한다.
#       이때 각 종류의 화폐는 몇 개라도 사용할 수 있다.
#       ex) 2원,3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.
#       M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하라.
#       입력 예시) 2 15 ,2,2 출력예시) 5
#       출력 예시) 3 4, 3, 5, 7 출력예시) -1
#       1<=N<=100 , 1<=M<=10000
N,M = map(int,input().split())
array = []
for i in range(N):
    array.append(int(input()))

d = [10001] * (M+1)

d[0] = 0
for i in range(N):
    for j in range(array[i],M+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j],d[j-array[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
