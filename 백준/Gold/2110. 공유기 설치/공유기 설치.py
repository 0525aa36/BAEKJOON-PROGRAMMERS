import sys

N, C = map(int, sys.stdin.readline().split())

array = []
for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()

def 이진탐색(array, start, end):
    while start <= end:
        mid = (start+end)//2
        현재 = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= 현재 + mid:
                count += 1
                현재 = array[i]
        
        if count >= C:
            global 최대거리
            start = mid + 1
            최대거리 = mid
        else:
            end = mid - 1


start = 1
end = array[-1] - array[0]
최대거리 = 0

이진탐색(array,start,end)
print(최대거리)
    

        
