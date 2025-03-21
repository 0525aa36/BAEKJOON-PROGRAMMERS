import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    명령 = sys.stdin.readline().split()
    if 명령[0] == "push":
        stack.append(명령[1])
        
    elif 명령[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif 명령[0] == 'size':
        print(len(stack))

    elif 명령[0] == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif 명령[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
