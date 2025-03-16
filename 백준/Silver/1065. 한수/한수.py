import sys

n = int(sys.stdin.readline())
count = 0

def 한수(number):
    N_str = list(map(int, str(number)))

    if len(N_str) <= 2:
        return True
    차이 = int(N_str[0]) - int(N_str[1])

    for i in range(1, len(N_str)-1):
        if int(N_str[i]) - int(N_str[i+1]) != 차이:
            return False
    return True


def 한수세기(n):
    count = 0
    for j in range(1, n+1):
        if 한수(j):
            count += 1
    return count


print(한수세기(n))


        



