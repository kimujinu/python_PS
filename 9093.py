import sys


for i in range((int(input()))):
    temp = sys.stdin.readline().split()
    for j in temp:
        print(j[::-1],end=' ')