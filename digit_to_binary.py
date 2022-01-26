# 십진수 -> 이진수 변환

digit_data = int(input())
binary_data = ''
while digit_data > 0:
    binary_data = str(digit_data%2)+binary_data
    digit_data//=2

print(binary_data)