# 문제 : 강의실 배정
# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.
# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데,
# 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다.
# (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!
# 입력
# 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
# 이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)
# 출력
# 강의실의 개수를 출력하라.
import heapq

N = int(input())
st = []
for _ in range(N):
    s,t = map(int,input().split())
    st.append((s,t))
st.sort()
q = []
heapq.heappush(q,st[0][1]) # 처음 회의의 끝나는 시간 삽입

for i in range(1,N):
    if st[i][0] < q[0]: # 그 다음 인덱스의 회의 시작 시간과 그 전 인덱스의 회의 끝 시간을 비교하여 끝시간이 더 크다면 회의실 하나 더 개설
        heapq.heappush(q,st[i][1])
    else: # 회의실 계속 사용
        heapq.heappop(q)
        heapq.heappush(q,st[i][1])

print(len(q))