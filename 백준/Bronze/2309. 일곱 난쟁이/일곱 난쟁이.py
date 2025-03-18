import sys

난쟁이 = [int(sys.stdin.readline().strip()) for i in range(9)]

키 = sum(난쟁이)

가짜찾기 = False

for i in range(9):
    if 가짜찾기:
        break
    for j in range(i+1, 9):
        if 키 -(난쟁이[i]+난쟁이[j]) == 100:
            가짜1 = 난쟁이[i]
            가짜2 = 난쟁이[j]
            가짜찾기 = True
            break

난쟁이.remove(가짜1)
난쟁이.remove(가짜2)

난쟁이.sort()

for k in 난쟁이:
    print(k)