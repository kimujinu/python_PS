# 문제 : 이차원 배열과 연산
# 크기가 3×3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.
# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다.
# 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다.
# 행의 개수 < 열의 개수인 경우에 적용된다.
# 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다.
# 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
# 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다.
# 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며,
# 순서는 수가 먼저이다.
# 예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다.
# 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다.
# 다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다.
# 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.
# 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다.
# R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고,
# C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다.
# 행 또는 열의 크기가 커진 곳에는 0이 채워진다.
# 수를 정렬할 때 0은 무시해야 한다.
# 예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.
# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
# 배열 A에 들어있는 수와 r, c, k가 주어졌을 때,
# A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.
# 입력
# 첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)
# 둘째 줄부터 3개의 줄에 배열 A에 들어있는 수가 주어진다. 배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.
# 출력
# A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다.
# 100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력한다.

r, c, k = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(3)]

time = 0
def r_solve(row, col):
    max_len = 0
    for i in range(row):
        number_dict = dict()
        while a[i]:
            a_value = a[i].pop()
            if a_value == 0:
                continue
            if a_value in number_dict:
                number_dict[a_value] += 1
            else:
                number_dict[a_value] = 1

        sort_dict = sorted(number_dict.items(), key=lambda x: (-x[1], -x[0]))
        while sort_dict:
            a_value, a_count = sort_dict.pop()
            a[i].append(a_value)
            a[i].append(a_count)

        max_len = max(max_len, len(a[i]))

    for i in range(row):
        row_len = len(a[i])
        while row_len != max_len:
            a[i].append(0)
            row_len += 1


def c_solce(row, col):
    global a
    max_len = 0
    new_a = [list() for _ in range(col)]
    for j in range(col):
        number_dict = dict()
        for i in range(row):
            if a[i][j] == 0:
                continue
            else:
                if a[i][j] in number_dict:
                    number_dict[a[i][j]] += 1
                else:
                    number_dict[a[i][j]] = 1
        sort_dict = sorted(number_dict.items(), key=lambda x: (-x[1], -x[0]))
        while sort_dict:
            a_value, a_count = sort_dict.pop()
            new_a[j].append(a_value)
            new_a[j].append(a_count)
        max_len = max(max_len, len(new_a[j]))
    for i in range(col):
        row_len = len(new_a[i])
        while row_len != max_len:
            new_a[i].append(0)
            row_len += 1
    a = [[0] * len(new_a) for _ in range(len(new_a[0]))]
    for i in range(len(new_a)):
        for j in range(len(new_a[0])):
            a[j][i] = new_a[i][j]


def solve():
    global time, a
    while True:
        if time > 100:
            break
        if len(a) >= r and len(a[0]) >= c:
            if a[r-1][c-1] == k:
                break
        row = len(a)
        col = len(a[0])
        if row >= col:
            r_solve(row, col)
        else:
            c_solce(row, col)
        if len(a) > 100:
            a = a[:100]
        if len(a[0]) > 100:
            for i in range(len(a)):
                a[i] = a[i][:100]
        time += 1

solve()

if time > 100:
    print(-1)
else:
    print(time)