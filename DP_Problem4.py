# 문제 : 금광
#       n * m 크기의 금광이 있다. 금광은 1 * 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어있다.
#       채굴자는 첫 번째 열 부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
#       이후에 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중에서 하나의 위치로 이동해야한다.
#       결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라.
#       ex) 1   3   3   2
#           2   1   4   1
#           0   6   4   7   이 경우 얻을 수 있는 금의 최대크기는 19이다. 2 -> 6 -> 4 -> 7
#       첫 번째줄에 테스트 케이스 T가 입력된다.
#       매 테스트 케이스 첫째 줄에 n과m이 공백으로 구분되어 입력된다.(1<=n,m<=20)
#       둘째 줄에 n*m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력된다.
#       입력 예시
#       2
#       3 4
#       1 3 3 2 2 1 4 1 0 6 4 7
#       4 4
#       1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
#       츌력 예시
#       19
#       16

for T in range(int(input())):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    dp = [] # dp테이블 생성
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
    print(result)