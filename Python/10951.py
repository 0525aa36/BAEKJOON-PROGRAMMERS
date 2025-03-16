import sys
T = int(sys.stdin.readline())


for i in range(T):
    while True:
        try:
            a,b = map(int, sys.stdin.readline().split())
        except:
            break
        print(a+b)
