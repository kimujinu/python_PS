# 문제 : 부분 문자열
# 길이가 K인 문자열 S가 있을 때, S의 연속된 일부분을 부분 문자열이라고 한다.
# 부분 문자열은 원래의 순서가 바뀌거나 중간에 있는 글자가 빠져서는 안된다.
# 주어진 문자열의 부분 문자열을 사전순으로 정렬한 후,
# N번째 부분 문자열의 첫 글자와 글자 수를 출력하는 프로그램을 완성하시오.
# 예를 들어 abac의 부분 문자열은 사전순으로 정렬하면 다음과 같다.
# a ab aba abac ac b ba bac c
# 3번째 부분 문자열은 aba가 된다.
# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 다음 줄부터 각 줄에 N과 문자열이 주어진다.
# 문자열의 길이는 4글자 이상 1000글자 이내이고, N은 문자열의 길이 이내이다. ( 1<=T<=50 )
# 3
# 5 abac
# 9 ltsodjxzyc
# 21 jldgovukjf
# [출력]
# #1 a 2
# #2 j 2
# #3 j 4
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
import sys


def calc_lcp(A, B):
    min_len = min(len(A), len(B))

    for c in range(min_len):  # A와 B를 비교해, 처음부터 연속된 같은 글자의 수가 LCP
        if A[:c + 1] != B[:c + 1]:
            break
    return c


def find_n_th_substring(suffix, n, max_len):
    lcp = 0
    i = 0

    while i < len(suffix):
        cur_idx, cur_suffix = suffix[i]
        candidate_num = max_len - cur_idx

        if candidate_num - lcp >= n:
            return cur_suffix[:n + lcp]
        else:
            n -= candidate_num - lcp
            if i != len(suffix) - 1:
                lcp = calc_lcp(cur_suffix, suffix[i + 1][1])
            i += 1
    return 0, 0


for tc in range(1, int(input()) + 1):
    N, string = input().split()
    N = int(N)

    suffix_unordered = [(i, string[i:]) for i in range(len(string))]
    suffix_ordered = sorted(suffix_unordered, key=lambda x: x[1])

    prefix = find_n_th_substring(suffix_ordered, N, len(string))
    print("#{} {} {}".format(tc, prefix[0], len(prefix)))