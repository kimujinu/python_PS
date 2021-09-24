# 소수(prime_number) : 1보다큰 자연수 중에서 1과 자기자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수
import math

# 소수 판별 함수 (2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수아님
    return True #소수

print(is_prime_number(4))
print(is_prime_number(7))

# 성능 분석 : 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있다.
#            ex) 2 * 8 = 16 , 8 * 2 = 16
#            따라서 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 된다.
#            2부터 X의 제곱근 까지의 모든 자연수 연산을 수행, O(N^1/2)