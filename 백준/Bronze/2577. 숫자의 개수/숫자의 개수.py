
A = int(input())
B = int(input())
C = int(input())
X = list(str(A * B * C)) # 곱셈값 숫자 하나하나 문자열로 list

for i in range(10):
    print(X.count(str(i))) # 문자열로 저장된 숫자를 카운트 해야해서 str(i)로 해야함