A, B = input().split()

RA = int(A[::-1])
RB = int(B[::-1])
if RA > RB:
    print(RA)
else:
    print(RB)