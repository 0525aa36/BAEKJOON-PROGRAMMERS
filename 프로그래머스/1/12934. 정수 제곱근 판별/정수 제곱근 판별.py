def solution(n):
    for x in range(1, n+1):
        if n == x**2:
            return (x+1)**2
    return -1
