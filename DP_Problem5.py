# 문제 : 병사 배치하기
#       N명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있다.
#       병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 도록 내림차순으로 배치하고자 한다.
#       다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다.
#       또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다.
#       그러면서도 남아 있는 병사의 수가 최대가 되도록 하고 싶다.
#       입력 조건 : 첫째 줄에 N이 주어진다.(1<=N<=2000)
#                  둘째 줄에 각 병사의 전투력이 공백으로 구분되어 차례대로 주어진다.
#       출력 조건 : 첫째 줄에 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력한다.
#       입력 예시 : 7
#                 15 11 4 8 5 2 4
#       출력 예시 : 2

N = int(input())
array = list(map(int,input().split()))

dp = [1] * N

# 순서를 뒤집어 최장 증가 부분 수열 문제로 변환
array.reverse()

# 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS) 알고리즘 수행
for i in range(1,len(array)):
    for j in range(0,i):
        if array[i]>array[j]: # 이전 원소와 비교
            dp[i] = max(dp[i],dp[j]+1)

# 열외해야 하는 병사의 최소 수
print(N-max(dp))

# 최장 증가 부분 수열(LIS) 알고리즘 : 원소가 n개인 배열의 일부 원소를 골라내서 만든 부분 수열중,
#                                 각 원소가 이전 원소보다 크다는 조건을 만족하고,
#                                 그 길이가 최대인 부분 수열을 최장 증가 부분수열 이라고한다.
#                                 ex) {6,2,5,1,7,4,8,3}이라는 배열이 있을 경우 LIS는 {2,5,7,8}이 된다.