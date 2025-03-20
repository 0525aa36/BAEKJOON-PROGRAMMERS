import sys

N, M = map(int, sys.stdin.  readline().split()) # 나무의 수, 가져 갈
tree = list(map(int, sys.stdin.readline().split())) # 나무 높이
start, end = 1, max(tree)  # 절단기 높이 범위

while start <= end: # 이분탐색
    mid = (start + end) // 2 # 절단기 높이
    tree_sum = 0 
    for i in tree: 
        if i > mid: # 절단기 높이보다 나무가 높으면
            tree_sum += i-mid # 절단기 높이만큼 잘라
    
    if tree_sum >= M: 
        start = mid + 1 # 절단기 높이 UP
    else:
        end = mid - 1 # 절단기 높이 DOWN
print(end)