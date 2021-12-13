# 문제 : 접두어 검색
# 문자열 about에서 첫 글자부터 이어지는 a, ab, abo, abou, about은 접두어이다.
# 단, abu 같이 첫 글자부터 계속 이어지는 경우가 아니면 접두어가 아니다.
# 문자열 그룹 A와 B가 주어질 때, B에 속한 문자열 중 A의 접두어인 문자열의 개수를 알아내는 프로그램을 만드시오. 모든 단어는 소문자로 이루어져 있다.
# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고,
# 테스트 케이스 별로 첫 줄에 A의 단어 개수 N과 B의 단어개수 M이 주어진다.
# 다음 줄부터 N개의 단어와 M개의 단어가 주어진다.
# 2
# 3 3
# able
# abl
# abroad
# ab
# abo
# a
# 3 5
# people
# water
# night
# wa
# h
# country
# ni
# people
# ( 1<=T<=50, 3<=N, M<=3000 )
# 단어의 길이는 20글자 이내이다.
# [출력]
# #1 2
# #2 3
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
import sys

for _ in range(int(input())):
    N,M = map(int,input().split())
    A = []
    result = 0
    for _ in range(N):
        A.append(sys.stdin.readline().rstrip())
    for _ in range(M):
        temp = sys.stdin.readline().rstrip()
        for i in A:
            if temp == i[0:len(temp)]:
                result += 1
                break
    print(result)
