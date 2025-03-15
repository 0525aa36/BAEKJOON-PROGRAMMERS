A = []
for i in range(9): #9개의 서로 다른 자연수가 주어질 때,
    a = int(input()) #리스트에 넣는 것 9번 반복
    A.append(a) #데이터 추가

print(max(A)) #max() 최댓값
print(A.index(max(A))+1) #최댓값 index : 0부터 시작하니 +1