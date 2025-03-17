import sys
data = sys.stdin.read().split()
N = int(data[0])
a = list(map(int, data[1:]))

a.sort()

for i in a:
    print(i)
    

