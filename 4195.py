# 문제 : 친구 네트워크
# 민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다.
# 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.
# 어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때,
# 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
# 친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.
# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.
# 2
# 3
# Fred Barney
# Barney Betty
# Betty Wilma
# 3
# Fred Barney
# Betty Wilma
# Barney Betty
# 출력
# 2
# 3
# 4
# 2
# 2
# 4
# 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
import sys

def find_parents(parent,x):
    if parent[x] != x:
        parent[x] = find_parents(parent,parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parents(parent,a)
    b = find_parents(parent,b)
    if a != b:
        parent[a] = b
        c_par[b] += c_par[a]
    print(c_par[b])

for _ in range(int(input())):
    F = int(input())
    parent = [i for i in range(F*2)]
    c_par =  [1]*(F*2)
    count = 0
    dict = {}
    for _ in range(F):
        A,B = sys.stdin.readline().split() # 해당 이름에다가 특정한 번호를 매칭
        if A not in dict:
            dict[A] = count
            count += 1
        if B not in dict:
            dict[B] = count
            count += 1
        union_parent(dict[A],dict[B])
