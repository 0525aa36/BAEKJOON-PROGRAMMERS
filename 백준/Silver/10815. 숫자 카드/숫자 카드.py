import sys


N = int(sys.stdin.readline().strip()) # 상근이 카드개수
N_cards = set(map(int, sys.stdin.readline().split())) #상근이카드


M = int(sys.stdin.readline().strip()) #확인카드개수
queries = list(map(int, sys.stdin.readline().split())) # g확인카드


result = [] # 상근이 카드랑 확인카드 있으면 1 없으면 0
for q in queries:
    if q in N_cards:
        result.append("1")
    else:
        result.append("0")


print(' '.join(result))

