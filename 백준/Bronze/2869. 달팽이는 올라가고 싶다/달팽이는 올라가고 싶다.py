import sys
A, B, V = map(int, sys.stdin.readline().split())

if (V-B) % (A-B) ==0: # 나머지가 생기면 하루 더 올라가야함
    print((V-B) // (A-B)) # 낮에 올라 갈 떄
else: 
    print((V-B) // (A-B)+1) # 낮에 못올라 갈 때(하루 +1)
