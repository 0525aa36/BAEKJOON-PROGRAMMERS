from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    # strip()으로 개행문자 제거, 각 문자를 정수로 변환
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 올바른 범위 검사: nx, ny가 0 <= index < n, m 이어야 함
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]

print(bfs(0,0))
