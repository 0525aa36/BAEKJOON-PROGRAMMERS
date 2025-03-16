import sys
#재귀함수
def 팩토리얼(n): # 3! = 3*2*1
    if n>1:
        return n * 팩토리얼(n-1)
    else:
        return 1
n = int(sys.stdin.readline())
print(팩토리얼(n))