# 힙(Heap) : 우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조
#               삽입시간    삭제시간
# 성능 : 리스트     O(1)      O(N)
#         힙      O(logN)   O(logN)

import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
