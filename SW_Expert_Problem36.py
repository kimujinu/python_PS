# 문제 : 이미지 유사도 검사 (DP, LCS(Longest Common Subsequence, 최장 공통 부분 수열)
# 이미지를 스캔하여 빨강(R), 녹색(G), 파랑(B), 검정(K)의 네 가지 색(코드)의 열로 반환해 주는 스캐너가 있다고 하자.
# 두 이미지의 스캔 코드열을 비교하여 유사도를 검사하고자 한다.
# 두 이미지의 스캔 코드열은 이미지 변질로 인하여 기본적으로 다음의 4가지 상태 중 하나의 상태를 갖는다.
# {일치(match), 불일치(mismatch), 삽입(insertion), 삭제(deletion)}
# 예를 들어 이미지 스캔 코드 열 X = “RBKBGRBGGG”와 Y = “BGKRBRKBGB”가 입력 될 경우에 대하여 살펴보면
# 이 중 일치하는 코드 열의 개수는 6인 것을 알 수 있다.
# 따라서 길이 10에서 6개가 일치하므로 60.00%의 유사도를 갖는다.
# 두 이미지 스캔 코드열을 입력 받아 유사도를 구하는 프로그램을 작성하시오.
# 예를 들어 위의 예에서 X의 부분 코드 열은 { {R},{B},…,{BK},…,{BKB},…,{BKBRBG},…,{RBKBGRBGGG}}이고
# Y의 부분 코드 열은 {{B},{G},…,{BK},…,{BKB},…,{BKBRBG},…,{BGKRBRKBGG}} 이다.
# 이들 중 공통 부분 열은 {{B}, …, {BK},…,{BKB},…,{BKBRBG}} 를 구할 수 있다.
# 이 중 가장 큰 공통 부분 코드열은 {BKBRBG}이면 크기는 6이다.
# 따라서 전체 크기에 따른 유사도는 6(일치)/10(전체크기)*100(백분율) = 60.00이다.
# [입력]
# 맨 위의 줄에는 전체 테스트 케이스의 수 T가 주어진다.
# 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스는 세 줄에 걸쳐 주어진다.
# 첫째 줄에는 이미지 스캔 코드열의 크기 N(단 N <= 500)이 주어지며 두 번째 줄에는 첫 번째 코드 열 X, 세 번째 줄에는 두 번째 코드 열 Y가 주어진다.
# 10
# 10
# RBKBGRBGGG
# BGKRBRKBGB
# 20
# BGBBRRKKRRGGRRBGGRBK
# BGBGBKGBBKKRKGBBKGRR
# 30
# BGBBRRKKRRGGRRBGGRBKBGBGBKGBBK
# KRKGBBKGRRGGKKBBBBKBGRBGRRRBGR
# 40
# RGGRRBGGRBKBGBGBKGBBKKRKGBBKGRRGGKKBBBBK
# BGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGB
# 50
# BGGRBKBGBGBKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRB
# RGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBG
# 80
# BBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBG
# RRGBBBBKBKKRRGRBBRKBGRRRRRKKBGRRBBGRBBRRKGRBRBKBBRBBGGRRBGBGGBBBKKKRRRKRKBBKBGGB
# 100
# GBKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBGRRGBBBBKB
# KKRRGRBBRKBGRRRRRKKBGRRBBGRBBRRKGRBRBKBBRBBGGRRBGBGGBBBKKKRRRKRKBBKBGGBKRRRRRKKRRRKGRRBRKRRKBRBBGRGB
# 150
# BGBBRRKKRRGGRRBGGRBKBGBGBKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBGRRGBBBBKBKKRRGRBBRKBGRRRRRKKBGRRBBGR
# BBRRKGRBRBKBBRBBGGRRBGBGGBGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRRRRRGRBRGGGBBRBBKRKRKBKKRRKRGGGBBRBBGBGGBRBGRBKBBKRBGBRBGBRBRBRBRBRBGBRBBBRRRBGRBRGRRGBRR
# 200
# BKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBGRRGBBBBKBKKRRGRBBRKBGRRRRRKKBGRRBBGRBBRRKGRBRBKBBRBBGGRRBGBGGBBBKKKRRRKRKBBKBGGBKRRRRRKKRRRKGRRBRKRRKBRBBGRGBK
# KBBKRKRRGBRKRRGBRBRKRKGBRBRKRBGBRBGBRBRBRBRBRBGBRBBBRRRBGRBRGRRGBRRBBBKBRBRBGBRBRBGBKBRBBKRRBBBBBRBBBKBRRBGRKBBBGRRRBBBBRBRBBBRBBRBBKBRKRKBBBRBBRBBRRRRKBRKRBGKRRBKRRBGKKGKBRRGGBBRKGRBBKRKKBBBBBRBBRKBB
# 500
# BGBBRRKKRRGGRRBGGRBKBGBGBKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBGRRGBBBBKBKKRRGRBBRKBGRRRRRKKBGRRBBGRBBRRKGRBRBKBBRBBGGRRBGBGGBBBKKKRRRKRKBBKBGGBKRRRRRKKRRRKGRRBRKRRKBRBBGRGBKKBBKRKRRGBRKRRGBRBRKRKGBRBRKRBGBRBGBRBRBRBRBRBGBRBBBRRRBGRBRGRRGBRRBBBKBRBRBGBRBRBGBKBRBBKRRBBBBBRBBBKBRRBGRKBBBGRRRBBBBRBRBBBRBBRBBKBRKRKBBBRBBRBBRRRRKBRKRBGKRRBKRRBGKKGKBRRGGBBRKGRBBKRKKBBBBBRBBRKBBRBBRBBRRBRBBGBBGBRBBRKBBKKBBGRRRRRRBRBGBKBRRRGRGBKKBRRBBBGGRBBBBKBBBBKKBKKBR
# RKBBKRKBGBKKBGKGKKBGKBBBKKBRRKGKRKKRBKGKBRRBRKRKKRGKBBBKRBBGKBBGBBGKBGKGKBRBBGKBKGKRBGGRRKGBBBBKRGBGKGBKRBKRBKKBGGGRBRRRKBRRRGRKBRRGBKRKKRGBBBKRBBBGRGGKBBBBKBKBGKGBGBBGRKRRRRGRGGRKRGRBKRRKKRBRBKRKKBGGKKRRRKGRRBRKRRKBRBBGRGBKKBBKRKRRGBRKRRGBRBRKRKGBRBRKRBGBRBGBRBRBRBRBRBGBRBBBRRRBGRBRGRRGBRRBBBKBRBRBGBRBRBGBKBRBBKRRBBBBBRBBBKBRRBGRKBBBGRRRBBBBRBRBBBRBBRBBKBRKRKBBBRBBRBBRRRRKBRKRBGKRRBKRRBGKKGKBRRGGBBRKGRBBKRKKBBBBBRBBRKBBRBBRBBRRBRBBGBBGBRBBRKBBKKBBGRRRRRRBRBGBKBRRRGRGBKKBRRBBBGGRBBBBKBBBBKKBKKBR
# [출력]
# #1 60.00
# #2 55.00
# #3 56.67
# #4 67.50
# #5 64.00
# #6 65.00
# #7 64.00
# #8 79.33
# #9 65.50
# #10 84.80
# 총 T줄에 T개의 테스트 케이스 각각에 대한 답을 한 줄에 출력한다.
# 각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 두 이미지의 유사도의 값을 소수점 두 번째 자리까지 구하여 한 줄에 출력한다.
import sys
for _ in range(int(input())):
    N = int(input())
    result = 0
    data1 = sys.stdin.readline().rstrip()
    data2 = sys.stdin.readline().rstrip()
    graph = [[0]*(N+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            if data1[i] == data2[j]:
                graph[i+1][j+1] = graph[i][j] + 1
                result = max(result,graph[i+1][j+1])
            else:
                graph[i+1][j+1] = max(graph[i+1][j],graph[i][j+1])

    print(format(result/N*100,".2f"))

