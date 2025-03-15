N = int(input())

for i in range (N):
    OX = list(input())
    S = 0 # 점수 초깃값
    SS = 0 # 점수 합계
    for j in OX:
        if j == "O":
            S += 1  # "=+" 요지랄해서 20분 낭비함,,
        else:
            S = 0
        SS += S
        
    print(SS)


