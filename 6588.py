
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

while True:
    N = int(input())
    if N == 0:
        break
    for i in range(3,N-2,2):
        if is_prime_number(i):
            a = i
            b = N-a
            if is_prime_number(b):
                flag = True
                break
            else :
                flag = False
        else :
            flag = False
    if flag :
        print('{} = {} + {}'.format(N, a, b))
    else:
        print("Goldbach's conjecture is wrong.")
