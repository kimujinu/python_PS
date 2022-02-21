# 트리 순회

class TreeNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

# 전위 순회 : 루트 -> 왼쪽 -> 오른쪽
def pre_order(node):
    print(node.data,end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

# 중위 순회 : 왼쪽 -> 루트 -> 오른쪽
def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.data,end='')
    if node.right != '.':
        in_order(tree[node.right])

# 후위 순회 : 왼쪽 -> 오른쪽 -> 루트
def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.data,end='')


n = int(input())
tree = {}
for _ in range(n):
    data,l_node,r_right = input().split()
    tree[data] = TreeNode(data,l_node,r_right)

#print('전위 순회 : ',end=' ')
pre_order(tree['A'])
print()
#print('중위 순회 : ', end=' ')
in_order(tree['A'])
print()
#print('후위 순회 : ', end=' ')
post_order(tree['A'])


