a = int(input())
b = int(input())

b0 = a * (b%10) # 5
b1 = a * ((b//10)%10) # 8
b2 = a * (b//100) # 3
b3 = a * b

print(b0)
print(b1)
print(b2)
print(b3)
