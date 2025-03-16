import sys

가로, 세로 = map(int, sys.stdin.readline().split())
테스트 = int(sys.stdin.readline())
가로리스트 = [0,가로]
세로리스트  = [0,세로]

for i in range(테스트):
    xy, cut = map(int, sys.stdin.readline().split())
    if xy == 0: # 0이면 세로 점을 자르는거니깐 세로리스트에 넣고
        세로리스트.append(cut)
    else: # 1이면 가로 점을 자르는거니깐 가로리스트에 넣어 맞아? 맞아
        가로리스트.append(cut)

가로리스트.sort()
세로리스트.sort()

넓이 = 0
for i in range(1, len(가로리스트)):
    for j in range(1, len(세로리스트)):
        x = 가로리스트[i] - 가로리스트[i-1]
        y = 세로리스트[j] - 세로리스트[j-1]
        넓이 = max(넓이, x*y)
        
print(넓이)