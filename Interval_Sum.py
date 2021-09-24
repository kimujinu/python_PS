# 구간 합 문제 : 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
# 문제 설명 : N개의 정수로 구성된 수열이 있다.
#            M개의 쿼리(Query) 정보가 주어진다.
#               -> 각 쿼리는 Left와 Right으로 구성된다.
#               -> 각 쿼리에 대하여 [Left,Right]구간에 포함된 데이터들의 합을 출력해야 한다.
#           수행 시간 제한은 O(N+M)이다.
# 접두사 합(Prefix Sum) : 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
# 동작과정 : 1) N개의 수 위치 각각에 대하여 접두사 합을 계산하여 P에 저장한다.
#          2) 매 M개의 쿼리 정보를 확인할 때 구간 합은 P[Right] - P[Left-1]이다.

# 데이터의 개수 N과 데이터 입력받기
n = 5
data = [10,20,30,40,50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산(세 번째 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])

