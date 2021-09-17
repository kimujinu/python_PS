import math

# 소수 판별 함수(에라토스테네스의 체)
#def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
#    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
#    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
#        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
#            j = 2
#            while i * j <= n:
#                array[i * j] = False
#                j += 1

#    return [ i for i in range(2, n+1) if array[i] ]

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함
#print(is_prime_number(26))


# 기본적인 소수 판별 방법(2부터 n-1까지 돌려보기)
def is_prime_number(x):
    if x == 1:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인
    for i in range(2, int(x**0.5)+1):
        # x가 해당 수로 나누어떨어지면
        if x % i == 0:
            return False
    return True

N,M = map(int,input().split())
for i in range(N,M+1):
    if is_prime_number(i):
        print(i)

