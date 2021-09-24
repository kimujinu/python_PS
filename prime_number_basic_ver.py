# 소수(prime_number) : 1보다큰 자연수 중에서 1과 자기자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수

# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2,x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수

print(is_prime_number(4))
print(is_prime_number(7))

# 성능 분석 : 2부터 X-1까지의 모든 자연수에 대해 연산을 해야한다.O(X)