# 문졔 : 떡볶이 떡 만들기(파라메트릭 서치 유형)
# 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
# 절단기의 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다. 이걸 처리 안 해줘서 시간을 허비했다.
# 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
#
# <제한 사항>
# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1<=N<=1,000,000, 1<=M<=2,000,000,000)
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.
#
# <입력 예시>
# 4 6
# 19 15 10 17
#
# <출력 예시>
# 15

#2.체크포인트
#절단기의 높이(탐색 범위)가 1부터 10억까지의 정수 중 하나 > 이진 탐색
#중간값에서 절단한 떡의 길이와 필요한 떡의 길이를 비교하면서 떡이 더 필요하면 중간 값을 줄이고, 떡이 너무 많이 절단되면 중간 값의 길이를 늘리는 방식.

#3.해결 방법
#시작점(0), 끝점(가장 긴 떡의 길이), 중간점((시작점+종료점)//2)
#주어진 떡의 길이가 절단기 높이(중간점)보다 클 경우 절단 가능
#절단한 떡의 총 길이와 필요한 떡의 총 길이 비교
#절단한 떡의 길이가 부족할 경우 중간점을 줄인다. (왼쪽 탐색)
#떡의 양이 충분한 경우 덜 자를 수 있는지 확인해서 최대한 덜 잘라야 함. (오른쪽 탐색)


# 파라메트릭 서치 유형: 최적화 문제를 결정 문제(예 or 아니오)로 바꾸어 해결하는 기법
#               예시)특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
#               이진탐색을 이용하여 해결이 가능하다

n,m = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0

# 이진 탐색
while(start <= end):
    total = 0
    mid = (start+end)//2
    for i in array:
        if i > mid:
            total += i - mid
    if total < m :
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
