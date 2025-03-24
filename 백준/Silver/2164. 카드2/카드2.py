import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque([i for i in range(1, N+1)])

while(len(card)>1):
    card.popleft()
    card_down = card.popleft()
    card.append(card_down)

print(card[0])