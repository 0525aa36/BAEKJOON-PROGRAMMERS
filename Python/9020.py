import sys

def 소수(n):
    if n<2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

T = int(input())

for j in range (T):
    A = int(input())
    B = A//2
    C = A//2
    
    for k in range(A//2):
        if 소수(B) and 소수(C):
            print(B, C)
            break
        else:
            B -= 1
            C += 1
