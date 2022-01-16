# 문제 : 팰린드롬 만들기
# 임한수와 임문빈은 서로 사랑하는 사이이다.
# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.
# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다.
# 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.
import sys

data = sys.stdin.readline().rstrip()
str_list = [0]*26
odd = 0
result = ''
temp_str = ''
for i in data:
    str_list[ord(i)-65] += 1

for i in range(26):
    if str_list[i]%2 == 1:
        odd += 1
        temp_str = chr(i+65)
    result += chr(i+65) * (str_list[i]//2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(result+temp_str+result[::-1])