# 에이스타 알고리즘 : 초기노드(시작지점)에서 목표 노드(목표지점)까지의 경로를 찾는 그래프 탐색 알고리즘이다.
#                  다른 그래프 탐색 알고리즘과 다른 점은 얼마나 근접한 것인지를 평가하는데 휴리스틱(추정 거리) 함수를 사용한다는 것이다.
#
# 시간복잡도 : H에 따라 다르다.
# O(b^d), where d = depth, b = 각 노드의 하위 요소수
# heapqueue를 이용하면 길을 출력할 때 reverse를 안해도된다.
#
# F = G + H , 에이스타 알고리즘의 핵심값
# 이 3개의 변수는 노드를 추가할 때마다 값이 갱신된다.
# F = 출발 지점에서 목적지까지의 총 cost 합(현재까지 이동하는데 걸린 비용과 예상 비용을 합친 총 비용)
# G = 현재 노드에서 출발 지점까지의 총 cost
# H = Heuristic(휴리스틱), 현재 노드에서 목적지까지의 추정 거리
#     (사이에 방해물로 인해 실제 거리는 알지 못한다. 그들을 무시하고 예상거리를 도출한다. 여러 방법이 존재)
#
# 에이스타 알고리즘 특징 : 1) openList와 closeList라는 보조 데이터를 사용한다.
#                      2) F = G + H 를 매번 노드를 생성할 때마다 계산한다.
#                      3) openList에는 현재 노드에서 갈 수 있는 노드를 전부 추가해서 F,G,H를 계산한다.
#                          openList에 중복된 노드가 있다면, F값이 제일 작은 노드로 바꾼다.
#                      4) closeList에는 openList에서 F값이 가장 작은 노드를 추가시킨다.


class Node:
    def __init__(self,parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def heuristic(node, goal, D=1,D2=2 ** 0.5): # Diagonal Distance (맨해튼 거리)
    dx = abs(node.position[0] - goal.position[0])
    dy = abs(node.position[1] - goal.position[1])
    return D * (dx+dy) + (D2 - 2 * D) * min(dx,dy)

def aStar(maze,start,end):
    # startNode, endNode 초기화
    startNode = Node(None,start)
    endNode = Node(None,end)

    # openList, closedList 초기화
    openList = []
    closedList = []

    # openList에 시작 노드 추가
    openList.append(startNode)

    # endNode를 찾을 때 까지 실행
    while openList:

        # 현재 노드 지점
        currentNode = openList[0]
        currentIdx = 0

        # 이미 같은 노드가 openList에 있고, f 값이 더 크면
        # currentNode를 openList안에 있는 값으로 교체
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIdx = index

        # openList에서 제거하고 closedList에 추가
        openList.pop(currentIdx)
        closedList.append(currentNode)

        # 현재 노드가 목적지인 current.position 추가하고
        # current의 부모로 이동
        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                # maze 길을 표시하려면 주석 해제
                x,y  = current.position
                maze[x][y] = 7

                for i in range(len(maze)):
                    print()
                    for j in range(len(maze)):
                        print(maze[i][j], end=' ')
                print()

                path.append(current.position)
                current = current.parent
            return path[::-1] # reverse

        children = []
        # 인접한 xy좌표 전부
        for newPosition in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
            # 노드 위치 업데이트
            nodePosition = (
                currentNode.position[0] + newPosition[0], # x
                currentNode.position[1] + newPosition[1]  # y
            )

            # 미로 maze index 범위 안에 있어야함
            within_range_criteria = [
                nodePosition[0] > (len(maze)-1),
                nodePosition[0] < 0,
                nodePosition[1] > (len(maze[len(maze)-1])-1),
                nodePosition[1] < 0,
            ]

            if any(within_range_criteria): # 하나라도 true면 범위 밖
                continue

            # 장애물이 있으면 다른 위치 불러오기
            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            new_node = Node(currentNode,nodePosition)
            children.append(new_node)


        # 자식들 모두 loop
        for child in children:
            # 자식이 closedList에 있으면 continue
            if child in closedList:
                continue

            # f,g,h값 업데이트
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2)+((child.position[1]- endNode.position[1]) ** 2) # 사이에 방해물로 인해 실제 거리는 알지 못한다. 그들을 무시하고 예상거리를 도출한다. 여러 방법이 존재

            # child.h = heuristic(child,endNode) 다른 휴리스틱
            # print("position:", child.position) 거리 추정 값보기
            # print("from child to goal:",child.h)

            child.f = child.g + child.h # 현재까지 이동하는데 걸린 비용과 예상 비용을 합친 총 비용 = 시작점 A로부터 현재 사각형까지의 경로를 따라 이동하는데 소용되는 비용 + 현재 노드에서 목적지 B까지의 예상 이동 비용

            # 자식이 openLsit에 있고, g값이 더 크면 continue
            if len([openNode for openNode in openList
                    if child == openNode and child.g > openNode.g])>0:
                continue


            openList.append(child)

def main():
    # 1은 장애물
    maze = [[0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

    start = (0,0)
    end = (7,6)

    path = aStar(maze, start, end)

    print()
    print(path)

if __name__ == '__main__':
    main()
