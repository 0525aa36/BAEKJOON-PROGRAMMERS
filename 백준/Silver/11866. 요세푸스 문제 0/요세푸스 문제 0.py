import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

Ndeq = deque([i for i in range(1, N+1)])

ys = []

while len(Ndeq) !=0:
    Ndeq.rotate(-(K-1))
    ys.append(Ndeq.popleft())

print("<" + ", ".join(map(str, ys)) + ">")

