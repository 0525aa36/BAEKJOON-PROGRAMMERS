def solution(l, r):
    answer = []
    for i in range(l, r+1):
        check = True
        for j in str(i):
            if j != "5" and j != "0":
                check = False
                break
        if check == True:
            answer.append(i)
            
    if not answer:
        return[-1]
    
    return answer
    
 