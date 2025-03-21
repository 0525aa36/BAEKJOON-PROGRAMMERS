import sys

K = int(sys.stdin.readline())

stack = []

for _ in range(K):
    수 = int(sys.stdin.readline())
    if 수 == 0: # 재현이가 0 부르면 앞에 수를 뻄
        stack.pop()
    else: # 0 아니면 그냥 그 수 스택에 넣음
        stack.append(수)

print(sum(stack))
