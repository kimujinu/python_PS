# 이분 탐색
# 정렬되어 있는 배열에서 특정 데이터를 찾기 위해 모든 데이터를 순차적으로 확인하는 대신,
# 탐색 범위를 절반으로 줄여가며 찾는 탐색법

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target: # 찾은 경우
        return mid
    elif array[mid] > target: # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽으로 이동
        return binary_search(array,target,start,mid-1)
    else: # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        return binary_search(array,target,mid+1,end)

n,target = map(int,input().split()) # 10 7
array = list(map(int,input().split())) # 1 3 5 7 9 11 13 15 17 19

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

# 이진 탐색의 시간 복잡도 : 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2N에 비례한다.
#                       시간복잡도는 O(logN)