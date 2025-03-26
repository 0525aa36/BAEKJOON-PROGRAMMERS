def solution(code):
    result = ''
    mode = 0
    
    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                mode = 1
            else:
                if i % 2 == 0:
                    result += code[i]
        else:
            if code[i] == "1":
                mode = 0
            else:
                if i % 2 != 0:
                    result += code[i]
    if not result:
        return "EMPTY"
    return result