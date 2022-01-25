# 링크드리스트 구현

class Node: # 노드 객체 클래스
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self):
        print("링크드 리스트 만들기 시작")
        self.head = None
        self.length = 0

    def __del__(self):
        print("가비치 콜렉션 호출..")

    def addFirst(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self,data):
        cur = self.head
        if cur == None: # 헤드 포인터에 값이 없을때
            self.addFirst(data)
            return

        newNode = Node()
        newNode.data = data

        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        self.length += 1
        print("끝에 붙이기")

    def showList(self):
        print("인스턴스 ID 리스트 출력",self)
        print("[", end='')
        node = self.head
        while node:
            print(node.data,end=' ')
            node = node.next
        print("]")
        print("길이",self.length)

    def deleteNode(self,index): # 특정 인덱스 삭제
        prev = None
        cur = self.head
        index -= 1
        i = 0
        while cur.next != None and i < index:
            prev = cur
            print(cur.data, index)
            cur = cur.next
            i += 1
        if index == i:
            self.length -= 1
            if prev == None:
                self.head = cur.next
            else:
                prev.next = cur.next
        else:
            print("배열 초과")

    def search(self,data):
        index = 0
        cur = self.head
        while cur != None:
            if cur.data == data:
                print("찾았당",index)
                return
            cur = cur.next
            index += 1
        print("없넹..")

def main():
    print('[파이썬 링크드 리스트 구현]')
    print('1. 노드생성')
    myLList = LinkedList()

    myLList.append(999)

    myLList.addFirst(1)
    myLList.addFirst(2)
    myLList.addFirst(3)
    myLList.addFirst(4)
    myLList.showList()

    myLList.append(5)
    myLList.append(6)
    myLList.append(7)
    myLList.showList()

    myLList.deleteNode(1)
    myLList.deleteNode(1)
    myLList.deleteNode(1)
    myLList.showList()

    myLList.search(7)

    listA = "뒤에 추가"
    newList = LinkedList()
    newList.append(listA)
    newList.showList()


if __name__ == '__main__':
    main()




