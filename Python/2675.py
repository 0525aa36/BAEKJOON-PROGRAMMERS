T = int(input())
for i in range(T):
   C, W = input().split()
   
   for j in W:
      print(j*int(C), end='')
   print()
