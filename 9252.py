# 문제: LCS 2
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
# 입력
# ACAYKP
# CAPCAK
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다.
# 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
# 출력
# 4
# ACAK
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.
# LCS가 여러 가지인 경우에는 아무거나 출력하고,
# LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.
import sys

data1 = [0]+list(sys.stdin.readline().rstrip())
data2 = [0]+list(sys.stdin.readline().rstrip())
h,w = len(data1),len(data2)
dp = [[""]*w for _ in range(h)]
len_result = 0

for i in range(1,h):
    for j in range(1,w):
        if data1[i] == data2[j]:
            dp[i][j] = dp[i-1][j-1] + data1[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])



