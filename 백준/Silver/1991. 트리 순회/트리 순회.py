import sys

# 노드의 개수 입력받기
N = int(sys.stdin.readline().strip())

# 트리 정보를 저장할 딕셔너리: 각 노드에 대해 (왼쪽 자식, 오른쪽 자식) 튜플을 저장
tree = {}
for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    tree[node] = (left, right)

# 전위 순회, 중위 순회, 후위 순회 결과를 저장할 리스트
preorder_result = []
inorder_result = []
postorder_result = []

# 전위 순회 함수: (루트) (왼쪽) (오른쪽)
def preorder(node):
    if node == '.':  # 자식 노드가 없는 경우
        return
    preorder_result.append(node)
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위 순회 함수: (왼쪽) (루트) (오른쪽)
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    inorder_result.append(node)
    inorder(tree[node][1])

# 후위 순회 함수: (왼쪽) (오른쪽) (루트)
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    postorder_result.append(node)

# 루트는 항상 'A'
preorder('A')
inorder('A')
postorder('A')

print("".join(preorder_result))
print("".join(inorder_result))
print("".join(postorder_result))
