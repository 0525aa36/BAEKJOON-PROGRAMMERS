def solution(s):
    answer = False
    
    cp = s.count('p') + s.count('P')
    cy = s.count('y') + s.count('Y')
    
    if (cp == cy):
        answer = True
    
    return answer