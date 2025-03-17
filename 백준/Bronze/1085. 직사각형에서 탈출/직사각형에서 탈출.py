import sys
x,y,w,h = list(map(int,input().split()))

a = min(x,y,(w-x), (h-y))
print(a)