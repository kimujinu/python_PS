# 문제 : 애너그램
# 씬디는 애너그램(anagram) 프로그램을 만들어 줄 수 있는 남자를 좋아한다. 참고로 씬디는 매우 예쁘다.
# 애너그램 프로그램이란, 입력받은 영단어의 철자들로 만들 수 있는 모든 단어를 출력하는 것이다.
# 가령 "abc" 를 입력받았다면, "abc", "acb", "bac", "bca", "cab", "cba" 를 출력해야 한다.
# 입력받은 단어내에 몇몇 철자가 중복될 수 있다. 이 경우 같은 단어가 여러 번 만들어 질 수 있는데, 한 번만 출력해야 한다.
# 또한 출력할 때에 알파벳 순서로 출력해야 한다.
import sys

def backtracking(x,value):
    if x == len(temp):
        sys.stdout.write("".join(value)+"\n")
        return
    for i in range(26):
        if vis[i] == 0:
            continue
        vis[i] -= 1
        backtracking(x+1,value+chr(i+97))
        vis[i] += 1


for i in range(int(input())):
    temp = list(sys.stdin.readline().rstrip())
    vis = [0 for _ in range(26)]
    for i in temp:
        vis[ord(i)-97] += 1
    backtracking(0,"")


