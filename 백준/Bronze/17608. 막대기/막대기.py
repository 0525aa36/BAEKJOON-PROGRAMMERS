import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    stack.append(int(sys.stdin.readline()))

마지막 = stack[-1]
count = 1

for j in reversed(stack[:-1]): # 오른쪽에서 본다는걸 넣어줘야함 ㅜㅡㅜ
    if j > 마지막:
        count += 1
        마지막 = j
print(count)