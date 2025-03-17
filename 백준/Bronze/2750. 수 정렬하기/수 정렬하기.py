import sys
N = int(sys.stdin.readline())  #수의 개수

a =[] # 수 넣을 곳

for i in range(N):
    a.append(int(input())) # a에 수 넣기

sort_a = sorted(a) # 정렬

for i in range(len(sort_a)): # 정렬된거 출력
    print(sort_a[i])