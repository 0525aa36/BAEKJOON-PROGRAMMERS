import sys

N = int(sys.stdin.readline()) # 주어진 수 개수
data = list(map(int, sys.stdin.readline().split())) # 주어진 수
count  = 0 # 소수 개수

# 소수 : 1과 자기 자신만으로 나누어지는 1보다 큰 자연수
for i in data:
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0: 
                if i == j:
                    count += 1
                break

print(count)

# 왜 이해가 안되지 졸린가

