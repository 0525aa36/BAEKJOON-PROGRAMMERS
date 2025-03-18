import sys

N = int(sys.stdin.readline())

word = []
for i in range(N):
    word.append(sys.stdin.readline().strip())

중복제거 = list(set(word))

오름차순 = []
for i in 중복제거:
    오름차순.append((len(i), i))

답 = sorted(오름차순)

for 길이, 단어 in 답:
    print(단어)