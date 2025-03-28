import sys

N = int(sys.stdin.readline().strip())

tree = {}
for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    tree[node] = (left, right)

preorder_result = []
inorder_result = []
postorder_result = []

def preorder(node):
    if node == '.':
        return
    preorder_result.append(node)
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    inorder_result.append(node)
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    postorder_result.append(node)

preorder('A')
inorder('A')
postorder('A')

print("".join(preorder_result))
print("".join(inorder_result))
print("".join(postorder_result))