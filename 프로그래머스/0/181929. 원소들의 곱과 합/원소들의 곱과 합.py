def solution(num_list):
    s = 0
    x = 1
    
    for i in range(len(num_list)):
        s += num_list[i]
        x *= num_list[i]
        
    if x < s**2:
        return 1
    else:
        return 0
   
