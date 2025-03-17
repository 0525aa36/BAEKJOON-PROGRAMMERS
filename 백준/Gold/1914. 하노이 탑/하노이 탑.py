import sys
N = int(sys.stdin.readline())

이동 = 2 ** N - 1
print(이동)
if N <= 20:
    def 하노이(원판, 시작, 보조, 목표):
        if 원판==1:
            print(시작, 목표)
        else:
            하노이(원판-1, 시작, 목표, 보조)
            
            print(시작, 목표)

            하노이(원판-1, 보조, 시작, 목표)

    하노이(N, 1, 2, 3)