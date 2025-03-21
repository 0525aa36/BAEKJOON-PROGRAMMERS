import sys

K = int(input())

for i in range(K):
    stack = []
    괄호 = input()

    for j in 괄호:
        if j == '(': # ( 이면 append
            stack.append('(') 
        elif j == ')': 
            if len(stack) == 0: # ) 이면 stack에 아무것도 없을 때 넣어
                stack.append(')')
                break
            else: # 있으면 ( 만 있으니깐 ()가 돼서 POP
                stack.pop()

    if len(stack) != 0: # 남아있는건 ) <- 이 바보만 있어서 올바르게 구성되지 않으니깐 NO
        print("NO")
    else:
        print("YES") # 남아 있지 않으면 완벽
           
    