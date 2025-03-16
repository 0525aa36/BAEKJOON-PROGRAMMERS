import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
count = 0

# 소수 : 1과 자기 자신만으로 나누어지는 1보다 큰 자연수


for x in data:
    if x>1:
        for i in range(2, x+1):
            if x % i == 0:
                if x == i:
                    count += 1
                break
print(count)