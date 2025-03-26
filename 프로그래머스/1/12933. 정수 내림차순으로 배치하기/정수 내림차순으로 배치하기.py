def solution(n):
    re = list(str(n))
    re.sort(reverse = True)
    
    return int("".join(re))