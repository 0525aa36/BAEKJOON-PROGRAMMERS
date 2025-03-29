import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

# DFS
dfs_result = []
visited = [False] * (N+1)
def dfs(v):
    visited[v] = True
    dfs_result.append(v)
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

dfs(V)
print(" ".join(map(str, dfs_result)))

# BFS
bfs_result = []
visited = [False] * (N+1)
queue = deque([V])
visited[V] = True
while queue:
    v = queue.popleft()
    bfs_result.append(v)
    for w in graph[v]:
        if not visited[w]:
            visited[w] = True
            queue.append(w)

print(" ".join(map(str, bfs_result)))
