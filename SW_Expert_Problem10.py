# 문제 : 퀵 정렬
# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고,
# A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.
# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
# 5<=N<=1,000,000, 0 <= ai <= 1,000,000
# 2
# 5
# 2 2 1 1 3
# 10
# 7 5 4 1 2 10 3 6 9 8
# [출력]
# #1 2
# #2 6
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, , N/2번 원소를 출력한다.

def partition(left,right):
    if left >= right:
        return
    pivot = left
    i = left + 1
    j = right - 1
    while i <= j:
        while i <= j and data[pivot] >= data[i]:
            i += 1
        while i <= j and data[pivot] <= data[j]:
            j -= 1
        if i <= j:
            data[i],data[j] = data[j],data[i]
    data[pivot],data[j] = data[j],data[pivot]

    partition(left,j)
    partition(j+1,right)

for _ in range(int(input())):
    N = int(input())
    data = list(map(int,input().split()))
    left = 0
    right = len(data)
    partition(left,right)
    print(data[N//2])