# 문제 : 8진수 2진수
# 8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 8진수가 주어진다. 주어지는 수의 길이는 333,334을 넘지 않는다.
# 출력
# 첫째 줄에 주어진 수를 2진수로 변환하여 출력한다.
# 수가 0인 경우를 제외하고는 반드시 1로 시작해야 한다.

data = input()
result = ""

for i in range(len(data)):
    n = int(data[i])
    temp = ""
    while n != 0:
        temp += str(n%2)
        n //= 2

    if i != 0:
        while len(temp) < 3:
            temp = temp+"0"

    result += temp[::-1]

if not result:
    print(0)
else:
    print(result)