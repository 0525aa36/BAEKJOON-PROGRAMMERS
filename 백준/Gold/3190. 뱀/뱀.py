import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

alst = [tuple(map(int, sys.stdin.readline().split()))for _ in range(K)]

L = int(sys.stdin.readline())
dlst = [sys.stdin.readline().split() for _ in range(L)]

di, dj = [-1,0,1,0],[0,1,0,-1] # 시계방향 방향정의
dtbl = [0] *(10001) # 방향전환에 사용되는 룩업

for sec, turn in dlst:
    dtbl[int(sec)]=turn



dr = 1 #오른쪽 방향
snake = [(1,1)] # 좌측상단
ans = 0 # 0초

while True:
    ans += 1 # 1초 경과
    ci, cj = snake[0] # 현재 머리좌표
    ni, nj = ci+di[dr], cj+dj[dr] # 진행방향으로  한 칸 이동

    # 벽에 부딪혔거나, 뱀 몸에 부딪힌 경우
    if 1 <= ni<=N and 1<=nj<=N and (ni,nj) not in snake:
        snake.insert(0, (ni,nj)) # 머리위치[0]에 이동좌표 확장
        if (ni,nj) in alst:
            alst.remove((ni,nj))
        else:
            snake.remove((snake[-1])) # 꼬리 제거
        # 방향전환
        if dtbl[ans] == 'D': #우회전
            dr = (dr+1)%4
        elif dtbl[ans] =='L':
            dr = (dr+3)%4
    else: #종료
        break

print(ans)