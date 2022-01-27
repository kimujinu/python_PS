# 문제 : 부분 문자열 (KMP)
# 문자열 S의 부분 문자열이란, 문자열의 연속된 일부를 의미한다.
# 예를 들어, "aek", "joo", "ekj"는 "baekjoon"의 부분 문자열이고,
# "bak", "p", "oone"는 부분 문자열이 아니다.
# 문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 알아보자.
# 입력
# 첫째 줄에 문자열 S, 둘째 줄에 문자열 P가 주어진다.
# 두 문자열은 빈 문자열이 아니며, 길이는 100만을 넘지 않는다.
# 또, 알파벳 소문자로만 이루어져 있다.
# 출력
# P가 S의 부분 문자열이면 1, 아니면 0을 출력한다.
import sys

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

def make_table(pattern):
    length = len(pattern)
    table = [0] * length
    j = 0

    for i in range(1,length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def KMP(parent,pattern):
    table = make_table(pattern)
    parent_length = len(parent)
    pattern_length = len(pattern)

    j = 0
    for i in range(parent_length):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]
        if parent[i] == pattern[j]:
            if j == pattern_length - 1:
                return 1
            else:
                j += 1
    return 0

print(KMP(S,P))